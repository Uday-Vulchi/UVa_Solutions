def even_sum(n): 
    c = 2
    sum = 0
    i = 1
      
    
    while i <= n: 
        sum += c 
          
         
        c += 2
        i = i + 1
    return sum
   
n = int(input())
print("sum of first ", n, "even number is: ", 
      even_sum(n)) 
