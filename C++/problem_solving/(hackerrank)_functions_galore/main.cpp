#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>
#include <iomanip>
#include <sstream>

#define IS_INT (int(c) >= 48 && int(c) <= 57)
#define IS_UPPER (int(c) >= 65 && int(c) <= 90)
#define IS_LOWER (int(c) >= 97 && int(c) <= 122)

template <typename T> std::vector<T> input_items(int arg_count) {
  std::vector<T> items;
  T input;

  while (arg_count > 0) {
    arg_count--;

    std::cin >> input;
    items.push_back(input);
  }

  return items;
}
/*
 * Computes the log of an integer input base 10. The answer is the integer part
 * only. e.g. n = 1000, answer is 3. n = 850, answer is 2. n = 1000000, answer
 * is 6. n = 123456, answer is 5.
 *
 */
unsigned int func1(boost::multiprecision::cpp_int n) {
  unsigned int log = 0;

  while (n >= 10) {
    n /= 10;
    log++;
  }

  return log;
}

/*
 * Computes the floor of a double input. e.g. n = 12, answer is 12. n = 12.3,
 * answer is 12. n = 12.9, answer is 12.
 *
 */
int func2(double n) {
  if (n > 0)
    return int(n);
  return int(n) - 1;
}

/*
 * Computes the ceiling of a double input. e.g. n = 12, answer is 12. n = 12.3,
 * answer is 13. n = 12.9, answer is 13.
 *
 */
int func3(double n) { return func2(n) + 1; }

/*
 * Computes the ceiling of a double input. e.g. n = 12, answer is 12. n = 12.3,
 * answer is 13. n = 12.9, answer is 13.
 *
 */

/*
 *  Determines if a character input is alphanumeric ('0'-'9' or 'a'-'z' or
 * 'A'-'Z'), or not. Display either YES or NO.
 *
 */

std::string func4(char c) {
  if ((IS_INT) || (IS_UPPER) || (IS_LOWER)) {
    return "YES";
  }
  return "NO";
}

/*
 * Determines if a character input is a letter from the English Alphabet
 * ('a'-'z' or 'A'-'Z'), or not. Display either YES or NO.
 *
 */
std::string func5(char c) {
  if (IS_UPPER || IS_LOWER) {
    return "YES";
  }
  return "NO";
}

/*
 * Determines if a character input is an upper case letter ('A'-'Z'), or not.
 * Display either YES or NO.
 *
 */
std::string func6(char c) {
  if (IS_UPPER) {
    return "YES";
  }
  return "NO";
}

/*
 * Determines if a character input is a lower case letter ('a'-'z'), or not.
 * Display either YES or NO.
 *
 */
std::string func7(char c) {
  if (IS_LOWER) {
    return "YES";
  }
  return "NO";
}

/*
 * Gives the uppercase equivalent of a character input if it is a lower case
 * letter. Otherwise, it simply gives the same input character. Display the
 * character.
 *
 */
char func8(char c) {
  if (IS_UPPER)
    return c;
  return c - 32;
}

/*
 *
 * Gives the lowercase equivalent of a character input if it is an upper case
 * letter. Otherwise, it simply gives the same input character. Display the
 * character.
 *
 */
char func9(char c) {
  if (IS_LOWER)
    return c;
  return c + 32;
}

/*
 * Determines if a character input is a punctuation mark (only for this purpose,
 * we will consider the period, question mark, exclamation point, comma,
 * semicolon, and colon as punctuation marks).
 *
 */

std::string func10(char c) {
  std::vector<int> symbols = {33, 44, 46, 58, 59, 63};
  auto it = std::find(symbols.begin(), symbols.end(), c);
  if (it != symbols.end()) {
    return "YES";
  }
  return "NO";
}

int main() {
  unsigned int test_cases;
  unsigned int function_id;

  std::cin >> test_cases;
  std::cin >> function_id;

  while (test_cases > 0) {
    test_cases--;

    switch (function_id) {
    case 1 ... 14 | 20:
      switch (function_id) {
        int param;
      case 1:
        param = input_items<int>(1)[0];
        std::cout << func1(param) << std::endl;
        break;
      case 2:
        param = input_items<double>(1)[0];
        std::cout << func2(param) << std::endl;
        break;
      case 3:
        param = input_items<double>(1)[0];
        std::cout << func3(param) << std::endl;
        break;
      case 4:
        param = input_items<char>(1)[0];
        std::cout << func4(param) << std::endl;
        break;
      case 5:
        param = input_items<char>(1)[0];
        std::cout << func5(param) << std::endl;
        break;
      case 6:
        param = input_items<char>(1)[0];
        std::cout << func6(param) << std::endl;
        break;
      case 7:
        param = input_items<char>(1)[0];
        std::cout << func7(param) << std::endl;
        break;
      case 8:
        param = input_items<char>(1)[0];
        std::cout << func8(param) << std::endl;
        break;
      case 9:
        param = input_items<char>(1)[0];
        std::cout << func9(param) << std::endl;
        break;
      case 10:
        param = input_items<char>(1)[0];
        std::cout << func10(param) << std::endl;
        break;
      }

      break;
    }
  }

  return 0;
}
