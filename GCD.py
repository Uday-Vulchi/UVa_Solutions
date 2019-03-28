#def computeGCD(x, y):
 #   if x > y:
  #      s = y
   # else:
    #    s = x
    #for i in range(1, s+1):
     #   if((x % i == 0) and (y % i == 0)):
         #   GCD = i        
    #return GCD
#num1 = int(input())
#num2 = int(input())
#print("The G.C.D. of", num1,"and", num2,"is", computeGCD(num1, num2))

def gcd(a,b): 
    if(b==0): 
        return a 
    else: 
        return gcd(b,a%b) 
  
a = int(input())
b= int(input())
  
print ("The gcd is : ",end=" ") 
print (gcd(a,b))
