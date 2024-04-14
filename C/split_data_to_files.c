#include "stdlib.h"
#include "time.h"
#include "stdio.h"
#include "stdint.h"
#include "errno.h"


int chars_to_int(uint32_t * number, char * string)
{
  char * endptr;

  errno = 0;

  unsigned long long_val = strtoul(string, &endptr, 10);
  if (errno != 0 || *endptr != '\0')
  {
    fprintf(stderr, "Invalid input: %s\n", string);
    return 1;
  }

  if (long_val > UINT32_MAX)
  {
    fprintf(stderr, "Value too large: %s\n", string);
    return 2;
  }

  *number = (uint32_t)long_val;

  return 0;
}

unsigned int file_length(unsigned int* length, FILE* file)
{

  if(fseek(file, 0, SEEK_END) != 0)
  {
    perror("Error seeking file!");
    return 1;
  }

  *length = ftell(file);
  if(*length == -1)
  {
    perror("Cannot get file size");
    return 2;
  }

}

uint32_t split_data(FILE* file, uint32_t bytes)
{
  uint32_t buffer[bytes];
  size_t bytes_read;
  FILE* part;

  int xor_bit = 0;
  uint32_t counter = 0;
  while((bytes_read = fread(buffer, 1, sizeof(buffer), file)) > 0)
  {
    char partname[10];
    sprintf(partname, "%04x", counter);
    xor_bit = rand() % 2;

    part = fopen(partname, "a+");


    if(xor_bit)
    {
      for(int i = 0; i < sizeof(buffer)/sizeof(buffer[0]); i++)
        buffer[i] ^= 0xFF;
      printf("XOR'd %s\n", partname);
    }
    if(fwrite(&xor_bit, 1, 1, part) != 1)
    {
      perror("Error writing XOR");
      fclose(part);
      return 1;
    }
    if(fwrite(buffer, 1, bytes_read, part) != bytes_read)
    {
      perror("Error writing to part file");
      fclose(part);
      return 1;
    }
    if (ferror(file))
    {
      perror("Error reading data");
      fclose(part);
      return 2;
    }

    fclose(part);
    counter++;
  }
  return 0;
}

int main(int argc, char *argv[])
{
  if (argc == 1)
  {
    fprintf(stderr, "Usage: %s <file> <bytes>\n", argv[0]);
    return 1;
  }

  // for(int i = 0; i < argc; i++){
  //   printf("%s\n", argv[i]);
  // }

  char *filename = argv[1];
  uint32_t bytes = 1;
  uint32_t SEED = 0;

  if (argc >= 3 && chars_to_int(&bytes, argv[2]) != 0)
      return EXIT_FAILURE;

  if (argc >= 4 && chars_to_int(&SEED, argv[3]) != 0)
      return EXIT_FAILURE;

  if (SEED == 0)
    srand(time(NULL));
  else
    srand(SEED);


  FILE *file;
  file = fopen(filename, "rb");

  if(file == NULL)
  {
    perror("ERROR");
    return EXIT_FAILURE;
  }



  unsigned int length = 0;
  file_length(&length, file);

  unsigned int iterations = length / (bytes * 4);

  if(fseek(file, 0, SEEK_SET) != 0)
  {
    perror("Failed to seek back");
    return EXIT_FAILURE;
  }



  printf("File size: %d bytes\n", length);
  printf("Files to be generated: %d\n", iterations);

  
  split_data(file, bytes);

  return EXIT_SUCCESS;
}
