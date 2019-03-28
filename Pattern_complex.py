size=int(input("enter size "))
int b[size][size]=1
left=0
top=size-1
n=1
#float i,j,left,top
for i in range (1,(size%2)):
    for j in range (left,top):
        n+=1
        b[left][j]=n
    for j in range (left+1,top):
        n+=1
        b[j][top]=n
    for j in range (left,top-1):
        n+=1
        b[top][j]=n
    for j in range (left+1,top-1):
        n+=1
        b[j][left]=n
for i in range (1,size):
    for j in range (i,size):
        print (b[i][j])
    print('')
    
        
