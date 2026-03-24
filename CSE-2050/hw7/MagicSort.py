from math import log2

def linear_scan(L):
    """runs through the list and counts how many elements are unordered compared to the next element
    tracks amount of unsorted elements and takes action based on that
    only goes through list once so the main algorithm time complexity is O(n)"""
    # these variables track the amount of unsorted elements
    unsorted = 0
    
    # goes through list and counts unsorted elements
    for i in range(len(L) - 1):
        if L[i] > L[i + 1]:
            unsorted += 1

    return unsorted
    

def reverse_list(L):
    """runs through the list from both ends and swaps elements until they reach the center
    only goes through list once so time complexity is O(n)"""

    # left pointer
    left = 0
    # right pointer
    right = len(L) - 1
    
    while left < right:
        # swaps elements at the left and right pointers
        L[left], L[right] = L[right], L[left]
        
        # moves left pointer to the right
        left += 1
        
        # moves the right pointer to the left
        right -= 1


def insertionsort(L, left = 0, right = None):
    """goes through list left to right and sorts elements with each other in place
    compares each element based on the sorted elements and inserts it in the right spot on the sorted side
    sorts in place"""
    if right == None:
        right = len(L)-1
    
    # goes through list
    for i in range(left, right):
        # starts at the end
        j = right-i-1
        
        # keeps swapping element and moving it down to the end until it's smaller than the next element on the sorted side
        while j < right and j+1 < len(L) and L[j] > L[j+1]:
            L[j], L[j+1] = L[j+1], L[j]
            j+=1
    

def quicksort(L, left=0, right=None, depth=0):
    """recursively sorts list by dividing and sorting and pulling back to top
    calls mergesort if recursion depth is too high
    calls insertionsort if less than 16 elements"""
    if right == None:
        right = len(L)
    
    # if there are less than 16 items left, switch to insertion sort
    if right - left <= 16:
        insertionsort(L, left, right)
        return L
    
    # if it's too much recursion, switch to merge sort
    if depth > 2*(log2(len(L))+1):
        mergesort(L, left, right)
        return L
    
    # makes last element pivot
    pivot = L[right]
    i = left - 1

    # loops through partition
    for j in range(left, right):
        if L[j] <= pivot:
            i += 1
            L[i], L[j] = L[j], L[i]
    
    # swaps pivot with the element at index i+1
    L[i+1], L[right] = L[right], L[i+1]

    # now goes down to divide each half
    quicksort(L, left, i, depth+1)
    quicksort(L, i+2, right, depth+1)


def mergesort(L, left = 0, right = None):
    """recursively cuts each list in half until there's only one element and adds them together in another function"""
    # if list is one element long
    if len(L) < 2: 
        return L
    
    # divdes
    mid = len(L) // 2
    A = L[:mid] 
    B = L[mid:]

    # recursvie 
    mergesort(A) 
    mergesort(B)

    # combine
    merge(A, B, L)

    
def merge(A, B, L):
    """takes two sorted sublists A and B and combines them into a single sorted list L"""
    i = 0 # index into A
    j = 0 # index into B

    # iterates through both sublists, comparing elements and appending the smaller one to L
    while i < len(A) and j < len(B): 
        if A[i] < B[j]:
            # append the smaller element from A to L
            L[i+j] = A[i]
            # moves to the next element in A
            i = i + 1 
        else:
            # appends the smaller element from B to L
            L[i+j] = B[j] 
            # moves to the next element in B
            j = j + 1 
            
    # adds any remaining elements once one list is empty 
    L[i+j:] = A[i:] + B[j:]

   
def magic_sort(lst):
    """supposed to sort in place?????
    if I can't I can't but I tried"""
    # keeps track of algorithms used
    sorts = set()

    # if there are no unsorted elements, it's linear
    if linear_scan(lst) == 0:
        sorts.add('linear')
        return sorts
    # if they're all unsorted, it's reverse
    elif linear_scan(lst) == len(lst) - 1:
        sorts.add('reverse_list')
        reverse_list(lst)
    # if there are less than 5 elements
    elif len(lst) < 5:
        sorts.add('insertionsort')
        insertionsort(lst)
    # otherwise go to quicksort
    else:
        quicksort(lst)
        if lst == 'mergesort':
            sorts.add('mergesort')
            sorts.add('insertionsort')
        else:
            sorts.add('quicksort')
            sorts.add('insertionsort')

    return sorts 


def is_sorted(L):
   '''Returns True (False) if L is (is not) sorted
   yoinked from hw6'''
   return not any(L[i] > L[i+1] for i in range(len(L)-1))