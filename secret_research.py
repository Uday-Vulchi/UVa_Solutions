T=int(input())
while(T):
    i=input()
    if (i == "1" or i == "4" or i == "78"):
        print('+')
    elif (i[len(i) - 2] == '3' and i[len(i) - 1] == '5'):
        print('-')
    elif (i[0] == '9' and i[len(i) - 1] == '4'):
        print('*')
    else:
        print('?')
    T-=1

    
