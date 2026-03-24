import time

def time_function(func, arg, n_trials = 10):
    """returns the smallest time it takes to run a function out of n trials"""
    times = []
    for i in range(n_trials): # iterates through n trials
        st = time.time() # takes the start time
        func(arg) # runs function
        et = time.time() # take the end time
        fi = et-st # get the time passed
        times.append(fi) # add it to list
    return (min(times)) # return the lowest time taken of the trials
    
def time_function_flexible(f, args, n_trials = 10):
    """returns how long it takes to run a function with unlimited parameters"""
    times = []
    for i in range(n_trials): # iterates through n trials
        st = time.time() # takes the start time
        f(*args) # runs function with extra (if it wants) arguments
        et = time.time() # take the end time
        fi = et-st # get the time passed
        times.append(fi) # add it to list
    return (min(times)) # return the lowest time taken of the trials

if __name__ == '__main__':
    # Some tests to see if time_function works
    def test_func(L):
        for item in L:
            item *= 2

    L1 = [i for i in range(10**5)]
    t1 = time_function(test_func, L1)

    L2 = [i for i in range(10**6)] # should be 10x slower to operate on every item
    t2 = time_function(test_func, L2)

    print("t(L1) = {:.3g} ms".format(t1*1000))
    print("t(L2) = {:.3g} ms".format(t2*1000))