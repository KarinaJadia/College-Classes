#include <iostream>
using namespace std;

void ECRemoveSpace(int nums[], int len, int val) {
    int end = len - 1;

    for (int i = 0; i <= end; ) {
        if (nums[i] == val) {
            // Swap with the element at 'end'
            nums[i] = nums[end];
            nums[end] = -1; // replace removed value with 0
            end--;
        } else {
            i++;
        }
    }
}