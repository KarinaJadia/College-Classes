#include <iostream>
using namespace std;

// complete the definition of the sorting function ...
void ECSortFP(int *listNumbers, int size, bool (*cmp)(int, int))
{
  // your code here
  for (int i = 0; i < size - 1; i++)
  {
    for (int j = i + 1; j < size; j++)
    {
        if (!cmp(listNumbers[i], listNumbers[j]))
        {
            int temp = listNumbers[i];
            listNumbers[i] = listNumbers[j];
            listNumbers[j] = temp;
        }
    }
  }
}

int main()
{
  int arr[] = {1,3,2,4};
  ECSortFP(arr, 4, [](int a, int b) { return a < b; });

  // print it out
  for(int i=0; i<4; ++i)
  {
    cout << arr[i] << " ";
  }
  cout << endl;

  ECSortFP(arr, 4, [](int a, int b) { return a > b; });

  // print it out
  for(int i=0; i<4; ++i)
  {
    cout << arr[i] << " ";
  }
  cout << endl;
}

