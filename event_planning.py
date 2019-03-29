T= int(input())
n=int(input())
while(n == 1):
    if(n==0):
        break
        T=0
        while(1):
            while(n!=0):
                T=T+(n%10)
                n=n/10;
                if(T/10==0):
                    break
                else:
                    n=T
                    T=0
                
        print(T)
n-=1