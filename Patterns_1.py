t=int(input())
ite=1
for j in range(t,0,-1):
    if ite%2!=0:
        for i in range(1,j+1):
            print(i,end=' ')
        print(' ')
    else:
        for i in range(j,0,-1):
            print(i,end=' ')
        print(' ')
    ite=ite+1
