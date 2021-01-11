
def maxSubarrayProblem(arr, low, middle, high) : 
       
    sum = 0; left_sum = -10000
      
    for i in range(middle, low-1, -1) : 
        sum = sum + arr[i] 
          
        if (sum > left_sum) : 
            left_sum = sum 
      
    sum = 0; right_sum = -1000
    for i in range(middle + 1, high + 1) : 
        sum = sum + arr[i] 
          
        if (sum > right_sum) : 
            right_sum = sum 
      
    return max(left_sum + right_sum, left_sum, right_sum) 
  
def maxSubArraySum(arr, low, high) : 
      
    if (low == high) : 
        return arr[low] 
  
    middle = (low + high) // 2
  
    return max(maxSubArraySum(arr, low, middle), 
               maxSubArraySum(arr, middle+1, high), 
               maxSubarrayProblem(arr, low, middle, high)) 
              
  
 
  
def Problems():

    arr = [2, 5, 7, 4, 10, -2, 0, 1]
    n = len(arr) 
    print("Array", arr)
    RunProblems(arr, n)
    arr2 = [2, 1, 3]
    n = len(arr2) 
    print("Array", arr2)
    RunProblems(arr2, n)
    arr3 = [9, 3, -6, 7, 2, 5, -10]
    n = len(arr3) 
    print("Array", arr3)
    RunProblems(arr3, n)
    
def RunProblems(array, n):
  
    print("Max Sub-Array Sum", maxSubArraySum(array, 0, n-1))
    
Problems()