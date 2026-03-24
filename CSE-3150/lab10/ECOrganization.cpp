// Code for modeling a university's various units: department, office,
// college, etc

// Generic interface. 
#include <vector>

class ECUnit
{
public:
  virtual ~ECUnit() {}
  virtual double GetBudget() const = 0;
};

// Department
class ECDepartment : public ECUnit
{
public:
  ECDepartment(int b) : budget(b) {}
  
  double GetBudget() const override
  {
    return budget;
  }

private:
  int budget;
};

// Office
class ECOffice : public ECUnit
{
public:
  ECOffice(int b) : budget(b) {}

  double GetBudget() const override
  {
    return budget;
  }

private:
  int budget;
};

// Composite
class ECCompositeUnit : public ECUnit
{
public:
  ECCompositeUnit() {}

  ~ECCompositeUnit()
  {
    for (ECUnit* p : children)
    {
      delete p;
    }
  }

  void AddChild(ECUnit *pUnit)
  {
    children.push_back(pUnit);
  }

  double GetBudget() const override
  {
    double sum = 0;
    for (ECUnit* p : children)
    {
      sum += p->GetBudget();
    }
    return sum;
  }

private:
  std::vector<ECUnit*> children;
};