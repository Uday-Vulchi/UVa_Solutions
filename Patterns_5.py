n=int(input("enter a number"))
count=1

for i in range (1,n+1):
    inc=3
    for j in range (1,i+1):
        print (count,end=' ')
        count+=inc
        inc-=1
    print('')
