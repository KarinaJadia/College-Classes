#include "ECTime.h"
#include <iostream>
using namespace std;

//your code goes here

ECTime::ECTime(int h, int m, int s) {
    hour = h;
    min = m;
    sec = s;
}

ECTime::~ECTime() {
}

void ECTime::GetTime(int &h, int &m, int &s) const {
    h = hour;
    m = min;
    s = sec;
}

ECTime ECTime::operator+(const ECTime &tmToAdd) {
    int totalSec = sec + tmToAdd.sec;
    int totalMin = min + tmToAdd.min;
    int totalHour = hour + tmToAdd.hour;

    if (totalSec >= 60) {
        totalSec -= 60;
        totalMin += 1;
    }

    if (totalMin >= 60) {
        totalMin -= 60;
        totalHour += 1;
    }

    return ECTime(totalHour, totalMin, totalSec);
}

int main()
{
  ECTime t1(0, 1, 30), t2(1, 2, 31);
  ECTime t3 = t1 + t2;
  int s, m, h;
  t3.GetTime(h, m, s);
  cout << "h: " << h << ", m: " << m << ", s: " << s << endl;
}
