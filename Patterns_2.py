n=int(input())
for i in range(0, n):
    for j in range(0, i+1):
        if j%2!=0:
            print("0 ",end="")
        else:
            print("1 ",end="")
    print("\r")
