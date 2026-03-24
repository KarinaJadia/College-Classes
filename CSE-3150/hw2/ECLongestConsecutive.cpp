#include <iostream>
#include <vector>

using namespace std;

int ECLongestConsecutive(vector<int>& nums) {
    // return the longest length of consecutive numbers in nums
    // Implement function here

    // sorts O(n^2) because i am stupid 💔
    if (nums.empty()) return 0;
    for (int i = 0; i < nums.size(); i++) {
        for (int j = i + 1; j < nums.size(); j++) {
            if (nums[j] < nums[i]) {
                int temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
            }
        }
    }

    int longest = 1;
    int current = 1;
    for (int i = 1; i < nums.size(); i++) {
        if (nums[i] == nums[i - 1]) {
            continue;
        } else if (nums[i] == nums[i - 1] + 1) {
            current++;
            if (current > longest) longest = current;
        } else {
            current = 1;
        }
    }

    return longest;
}