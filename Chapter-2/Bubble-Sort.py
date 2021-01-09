
def BubbleSort(Array):
    t = len(Array)
    for i in range(t):   
        change = False     
        for j in range(0, t-i-1):
            if Array[j] > Array[j+1]:
                temp = Array[j]
                Array[j] = Array[j+1]
                Array[j+1] = temp
                change = True
        if change == False:
            return Array
            

def Problems():
    arr = [2, 5, 7, 4, 10, -2, 0]
    print("Unsorted", arr)
    RunProblems(arr)
    arr2 = [2, 1, 3]
    print("Unsorted", arr2)
    RunProblems(arr2)
    arr3 = [9, 3, 6, 7, 2, 5, 10]
    print("Unsorted", arr3)
    RunProblems(arr3)
    
def RunProblems(array):
    print("Sorted", BubbleSort(array))
    
Problems()