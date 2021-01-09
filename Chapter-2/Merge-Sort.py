# Worst-Case Run-Time = O(n*log(n))
# Worst-Case Space-Complexity = O(n)
def MergeSort(A):
    
    L, R = split(A)
    if len(L) > 1:
        MergeSort(L)
    if len(R) > 1:
        MergeSort(R)
    
    i = 0
    j = 0
    k = 0
     
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i+1
        else:
            A[k] = R[j]
            j = j + 1
        k +=1
    
    while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1
 
    while j < len(R):
        A[k] = R[j]
        j += 1
        k += 1
    return A
    
    
 
def split(Array):
    split = len(Array) // 2
    return Array[:split], Array[split:]

def Problems():
    arr = [1, 2, 3, 4, 5]
    arr2 = [5, 4, 3, 2, 1]
    arr3 = [2, 3, 4, 5, 7, 2, 7, 3, 0, 1]
    arr4 = [3, 1, 2, 4]
    
    print("Problem 1", arr)
    RunProblems(arr)
    print("Problem 2", arr2)
    RunProblems(arr2)
    print("Problem 3", arr3)
    RunProblems(arr3)
    print("Problem 4", arr4)
    RunProblems(arr4)
    
def RunProblems(Array):

    print("Sorted", MergeSort(Array))
    
Problems()