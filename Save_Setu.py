t=int(input())
c=0
while (t):
    s=input()
    a=s.split()
    if(a[0]=="donate"):
        c+=int(a[1])
        
    else:
        print (c)
    t=t-1
        
    
