#include <stdio.h>

int validate_key(char* key){

  return 0;
};

int main()
{
  char serial_key[10];
  if (validate_key(serial_key)){
    printf("Key is valid.\n");
  }else{
    printf("Key is invalid.\n");
  }

  return 0;
}
