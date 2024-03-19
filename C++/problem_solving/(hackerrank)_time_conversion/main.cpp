
#include <bits/stdc++.h>
#include <iomanip>
#include <sstream>

/*
 * Complete the 'timeConversion' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */

std::string timeConversion(std::string s) {

  int hh, mm, ss;
  char c;

  std::stringstream time(s);

  time >> hh >> c >> mm >> c >> ss;

  if (s[8] == 'P') {
    if (hh <= 12) {
      hh += 12;
    }
  } else if (s[8] == 'A') {
    if (hh == 12) {
      hh = 0;
    }
  }

  std::ostringstream output;

  output << std::setfill('0') << std::setw(2) << hh << ":" << std::setfill('0')
         << std::setw(2) << mm << ":" << std::setfill('0') << std::setw(2)
         << ss;

  return output.str();
}

int main() {
  std::ofstream fout(getenv("OUTPUT_PATH"));

  std::string s;
  getline(std::cin, s);

  std::string result = timeConversion(s);

  fout << result << "\n";

  fout.close();

  return 0;
}
