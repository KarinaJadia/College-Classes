import time
import random

def find_pairs_naive(list, target):
    """iterates through list twice and tests each element to see what adds up to target, then returns a tuple"""
    # this is the list that will store the values (will be converted to tuple)
    lis = [] # 1
    for i in list: # n
        for j in list: # n
            # makes sure it is the correct sum and there are no duplicates
            if i != j and i+j==target and not([j, i] in lis): # 4
                lis.append([i, j]) # 1
    # converts main list to tuple
    return tuple(lis) # 1 + 4 + n * n = O(n^2)

def find_pairs_optimized(list, target):
    """uses a hash map to iterate through list and check if the elements add to target in constant time"""
    # this is the list that will store the values (will be converted to tuple)
    lis = [] # 1
    # the hash table that will store each number as a key
    num_map = {} # 1
    # iterates through the list once, which cuts the time complexity
    for num in list: # n
        # checks if target_sum - num is in the num_map and addes the pair (num, target_sum - num) to the result list
        if target - num in num_map: # 2
            lis.append([num, target - num]) # 1
        # if it's not in the list, the num is added to the num_map
        else: # 4? since the previous line won't execute if it's not true
            num_map[num] = True # 1
    return tuple(lis) # 1 + 1 + n + 2 + 1 = O(n)

def measure_min_time(fn, *args):
    """returns how long it takes to run a function with unlimited parameters"""
    times = []
    # iterates through n trials
    for i in range(0, 10):
        # takes the start time
        st = time.time()
        # runs function with extra (if it wants) arguments
        fn(*args)
        # take the end time
        et = time.time()
        # get the time passed
        fi = et-st
        # add it to list
        times.append(fi)
    # return the lowest time taken of the trials
    return (min(times))

if __name__ == '__main__':
    # i made this function just to not have to print the same ugly spaced out formatted lines multiple times
    def readability(x):
        """takes the generated list of x size and puts it into the time measuring function"""
        lis = list_generator(x)
        return(f' {x}           {measure_min_time(find_pairs_naive, lis, 15):.4f}            {measure_min_time(find_pairs_optimized, lis, 15):.4f}')
    
    def list_generator(x):
        """this is the random list generator for 'n' and is set to generate a list of random numbers 1-15 of given size"""
        lis = []
        for i in range(x):
            lis.append(random.randint(1, 15))
        return lis

    print('  n            naive            optimized')
    print('******************************************')
    # the spaces in the first two are to keep the double digit numbers in alignment
    print('',readability(10))
    print('',readability(50))
    print(readability(100))
    print(readability(150))
    print(readability(200))
    print(readability(300))
    print(readability(500))
    print('******************************************')