n=int(input('Enter n value'))
for i in range (0,n):
    k=(i*2)-1
    for j in range (i,n):
        k+=2
        print (k, end='')
    print('\n')
        

    