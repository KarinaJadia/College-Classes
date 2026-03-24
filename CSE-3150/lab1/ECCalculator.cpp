// Your code here

#include <iostream>
#include "ECNumbers.h"
using namespace ECNumbers;

namespace ECCalculator {

    int ECFourTimesN(int n) {
        return ECDoubleN(ECDoubleN(n));
    }

}