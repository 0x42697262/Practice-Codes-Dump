#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

/*
 * Complete the 'gradingStudents' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts INTEGER_ARRAY grades as parameter.
 */

vector<int> gradingStudents(vector<int> grades) {

  vector<int> rounded;

  int r;
  for (const int &grade : grades) {
    if (grade + 3 < 40) {
      rounded.push_back(grade);
      continue;
    }
    int rg = grade % 5; // 67 % 5 = 2
    if (rg < 3) {
      rounded.push_back(grade);
      continue;
    }

    int new_grade = grade - rg + 5;
    rounded.push_back(new_grade);
  }

  return rounded;
}

int main() {
  ofstream fout(getenv("OUTPUT_PATH"));

  string grades_count_temp;
  getline(cin, grades_count_temp);

  int grades_count = stoi(ltrim(rtrim(grades_count_temp)));

  vector<int> grades(grades_count);

  for (int i = 0; i < grades_count; i++) {
    string grades_item_temp;
    getline(cin, grades_item_temp);

    int grades_item = stoi(ltrim(rtrim(grades_item_temp)));

    grades[i] = grades_item;
  }

  vector<int> result = gradingStudents(grades);

  for (size_t i = 0; i < result.size(); i++) {
    fout << result[i];

    if (i != result.size() - 1) {
      fout << "\n";
    }
  }

  fout << "\n";

  fout.close();

  return 0;
}

string ltrim(const string &str) {
  string s(str);

  s.erase(s.begin(),
          find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace))));

  return s;
}

string rtrim(const string &str) {
  string s(str);

  s.erase(
      find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
      s.end());

  return s;
}
