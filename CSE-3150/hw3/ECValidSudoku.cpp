/*Instructions-
Return True/False if the sudoku board is valid
It is valid if:
	Each row contains non-duplicate values of 1-9
	Each column contains non-duplicate values of 1-9
	Each of the nine 3x3 sub-boxes of the board must contain non-duplicate values of 1-9

Note: "." represents a blank sudoku square
	  The board does not need to be solvable for it to be a valid board
	  You should be able to complete this with an O(n) time complexity
*/
#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>

using namespace std;


bool ECValidSudoku(vector<vector<string>> &board){
	
	//your code here

	// i know i probably did not follow the spirit of this assignment but i have already
	// solved it in python so i just translated my logic lol

	// (does anyone read these comments?)
	
	vector<unordered_set<string>> rows(9);
    vector<unordered_set<string>> cols(9);
    vector<unordered_set<string>> boxes(9);

    for (int r = 0; r < 9; r++) {
        for (int c = 0; c < 9; c++) {
            string val = board[r][c];

            if (val == ".") {
				continue;
			}

            int box = (r / 3) * 3 + (c / 3);
            if (rows[r].count(val) || cols[c].count(val) || boxes[box].count(val)) {
				return false;
			}

            rows[r].insert(val);
            cols[c].insert(val);
            boxes[box].insert(val);
        }
    }
	return true;

}