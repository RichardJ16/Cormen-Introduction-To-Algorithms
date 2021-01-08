#import numpy as np

def InsertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while (j >= 0 and arr[j] > key):
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key
    return arr
            
            

def RunProblems():

    arr = [25, 16, 2]
    print("Old Array: ", arr)
    arr = InsertionSort(arr)
    print("New Array: ", arr)
    
    arr2 = [20, 10, 5, 4, 3, 0, -1, 50]
    print("Old Array: ", arr2)
    arr2 = InsertionSort(arr2)
    print("New Array: ", arr2)
    
    arr3 = [10,590, -65, 2, 65, 3, 46, -89, 1002, 156]
    print("Old Array: ", arr3)
    arr3 = InsertionSort(arr3)
    print("New Array: ", arr3)
    
RunProblems()

# Array 2

# Starting on 10 looking at 20 index 1 comparing to index 0
# [20 10 5 4 3 0 -1 50]

# Swap Places
# [10 20 5 4 3 0 -1 50]

# Continue sorting parts that become unsorted
# [10 4 20 5 3 0 -1 50]
# [4 10 20 5 3 0 -1 50]

# [4 10 5 20 3 0 -1 50]
# [4 5 10 20 3 0 -1 50]

# [4 5 10 3 20 0 -1 50] ... [3 4 5 10 20 0 -1 50]

# [3 4 5 10 20 0 -1 50] ... [0 3 4 5 10 20 -1 50]

# [0 3 4 5 10 20 -1 50] ... [-1 0 3 4 5 10 20 50]