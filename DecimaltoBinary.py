def decimaltobinary(n):
   
   if n > 1:
       decimaltobinary(n//2)
   print(n % 2,end = '')


dec = int(input())
decimaltobinary(dec)
