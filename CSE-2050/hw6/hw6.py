# TODO: implement the 4 functions (as always, include docstrings & comments)

def find_zero(L):
    """divides the list in half multiple times to find where the zero is (time complexity is O log(n))"""
    # starts with both ends of the list
    left = 0
    right = len(L) - 1
    
    # repeats until target is found or the whole list has been searched
    # I'm so happy I can do this not-recursively
    while left <= right:
        mid = (left + right) // 2
        if L[mid] == 0:
            return mid
        elif L[mid] > 0:
            right = mid - 1
        else:
            left = mid + 1

    
def bubble(L, left, right):
    """goes through list and swaps elements based on whether they're smaller than the one before them, repeats through list until list is sorted"""
    """ this one doesn't work :( """
    for i in range(left, right+1):
        # this variable ensures that we don't keep going through the list if we're done, making best case time complexity O(n)
        swapped = True
        while swapped:
            swapped = False
            for j in range(left, right - i - 1):
                if L[j] > L[j+1]:
                    L[j], L[j+1] = L[j+1], L[j]
                    swapped = True


def selection(L, left, right):
    """goes through list, selects smallest element, swaps it to the sorted side and moves the boundary of sorted elements, repeats until fully sorted"""
    # iterates through list
    for i in range(left, right):
        min = i
        for j in range(i+1, right):
            # makes sure not to touch the sorted side
            if L[j] < L[min]:
                min = j
            # swaps smallest element with the one right next to the "wall" of sorted numbers
        L[i], L[min] = L[min], L[i]


def insertion(L, left, right):
    """goes through list left to right and sorts elements with each other, also kinda builds a wall but unlike selection doesn't take smallest element from whole list
    but instead compares each element based on the sorted elements and inserts it in the right spot on the sorted side"""
    # goes through list
    for i in range(left, right):
        # starts at the end
        j = right-i-1
        # keeps swapping element and moving it down to the end until it's smaller than the next element on the sorted side
        while j < right and L[j] > L[j+1]:
            L[j], L[j+1] = L[j+1], L[j]
            j+=1


def sort_halfsorted(L, sort):
    '''Efficiently sorts a list comprising a series of negative items, a single 0, and a series of positive items
    
        Input
        -----
            * L:list
                a half sorted list, e.g. [-2, -1, -3, 0, 4, 3, 7, 9, 14]
                                         <---neg--->     <----pos----->

            * sort: func(L:list, left:int, right:int)
                a function that sorts the sublist L[left:right] in-place
                note that we use python convention here: L[left:right] includes left but not right

        Output
        ------
            * None
                this algorithm sorts `L` in-place, so it does not need a return statement

        Examples
        --------
            >>> L = [-1, -2, -3, 0, 3, 2, 1]
            >>> sort_halfsorted(L, bubble)
            >>> print(L)
            [-3, -2, -1, 0, 1, 2, 3]
    '''

    idx_zero = find_zero(L)      # find the 0 index 
    sort(L, 0, idx_zero)         # sort left half
    sort(L, idx_zero+1, len(L))  # sort right half

#print(selection([-1,-5,3,2,5,1], 0, 6))