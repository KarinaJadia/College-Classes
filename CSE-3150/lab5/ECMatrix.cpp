// Note: you need to add compiler flag -fno-elide-constructors to
// disable copy elision (return value optimization) in order to see 
// move constructor work as what you expect
#include "ECMatrix.h" 
#include <iostream>

// default constructor
ECMatrix :: ECMatrix()
{
}

// create a matrix of nr rows and nc columns
ECMatrix::ECMatrix(int nr, int nc)
{
  // your code
  std::cout << "Parameterized constructor called\n";
  listElements = std::vector<std::vector<double>>(nr, std::vector<double>(nc, 0.0));
}

// Copy constructor
ECMatrix::ECMatrix(const ECMatrix &rhs)
{
  // your code
  std::cout << "Copy constructor called\n";
  listElements = rhs.listElements;
}

// 
ECMatrix ECMatrix::operator=(const ECMatrix &rhs) 
{
  // your code
  std::cout << "Copy assignment operator called\n";
  if (this != &rhs)
  {
    listElements = rhs.listElements;
  }
  return *this;
}

// Move constructor
ECMatrix::ECMatrix(ECMatrix &&rhs)
{
  // your code
  std::cout << "Move constructor called\n";
  listElements = std::move(rhs.listElements);
  rhs.listElements.clear();
}

// Get num of rows/columns
int ECMatrix:: GetNumRows() const
{
  // your code
  return listElements.size();
}

int ECMatrix :: GetNumCols() const
{
  // your code
  if (listElements.empty())
    return 0;
  return listElements[0].size();
}

// Get/set an element in the matrix
double ECMatrix::GetVal(int r, int c) const
{
  // your code
  return listElements[r][c];
}
void ECMatrix::SetVal(int r, int c, double val)
{
  // your code
  listElements[r][c] = val;
}

// Scale by a factor
ECMatrix ECMatrix:: Scale(double factor) const
{
  // your code
  std::cout << "Scale() called\n";
  ECMatrix result(GetNumRows(), GetNumCols());
  for (int i = 0; i < GetNumRows(); ++i)
  {
    for (int j = 0; j < GetNumCols(); ++j)
    {
      result.SetVal(i, j, GetVal(i, j) * factor);
    }
  }
  return result;
}

