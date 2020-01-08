
def bubblesort(array):
    count=0
    while True:
        swapped = False
        for i in range(len(array)-count-1):
            leftElement=array[i]
            rightElement=array[i+1]
            if leftElement>rightElement:
                array[i],array[i+1]=rightElement,leftElement
                swapped=True
        count+=1
        if swapped==False:
            break
    return array

def mergesort(array):
    #split each element into partitions of size 1
    a = []
    for i in array:
        a.append([array[i]])
    #recursively merge adjacent partitions
    for i in range(len(a)):
        
        if leftPartHeadValue <= rightPartHeadValue
            copy leftPartHeadValue
        else:
            copy rightPartHeadValue
    copy elements back to original array


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print bubblesort(test)

"""Implement quick sort in Python.
Input a list.
Output a sorted list.
def quicksort(array):
    for each(unsorted) partition
    set first element as pivot
    storeIndex = pivotIndex + 1
    for i = pivotIndex + 1 to rightmostIndex
        if element[i] < element[pivot]
            swap(i, storeIndex);
            storeIndex++
    swap(pivot, storeIndex - 1)

def insertionsort(array):
    mark first element as sorted
    for each unsorted element X
    'extract' the element X
        for j = lastSortedIndex down to 0
            if current element j > X
                move sorted element to the right by 1
            break loop and insert X here




def selectionsort(array):
    repeat(numOfElements - 1) times
        set the first unsorted element as the minimum
        for each of the unsorted elements
            if element < currentMinimum
                set element as new minimum
        swap minimum with first unsorted position

"""

