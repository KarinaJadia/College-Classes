#include "ECShapes.cpp"
#include <iostream>
using namespace std;

template <typename T>
void Area(Shape<T> &s) {
    cout << "Area: " << s.CalcArea() << endl;
}

void Test1()
{
  Rectangle<int> r1(10,5);
  Area(r1);
  Square<int> s1(10);
  Area(s1);
}

// now test with custom object
// MyNum class has a custom constructor that takes a single integer
// Essentially MyNum is just like an intger and so it is not very useful on its own
// but we just want to test out template class 
class MyNum
{
public:
  MyNum(int x) : xv(x) {}
  // WHAT ELSE NEEDED?
  bool operator>=(const MyNum &other) const { return xv >= other.xv; }

  MyNum operator*(const MyNum &other) const { return MyNum(xv * other.xv); }

  MyNum operator-(const MyNum &other) const { return MyNum(xv - other.xv); }

  MyNum operator-() const { return MyNum(-xv); }

  friend MyNum abs(const MyNum &num) { return (num.xv < 0) ? MyNum(-num.xv) : num; }

  friend ostream &operator<<(ostream &os, const MyNum &num)
  {
    os << num.xv;
    return os;
  }

private:
  int xv;
};

void Test2()
{
  cout << "Test2\n";
  MyNum n1(10), n2(5);
  Rectangle<MyNum> r(n1, n2);
  Area(r);
}

int main()
{
  Test1();
  Test2();
}