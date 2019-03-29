def SubArrays(arr, start, end): 
      
   
    if end == len(arr): 
        return
      
    
    elif start > end: 
        return SubArrays(arr, 0, end + 1) 
          
    
    else: 
        print(arr[start:end + 1]) 
        return SubArrays(arr, start + 1, end) 
          

arr = list()
num = raw_input("Enter how many elements you want:")
print 'Enter numbers in array: '
for i in range(int(num)):
    n = raw_input("num :")
    arr.append(int(n))
SubArrays(arr, 0, 0)