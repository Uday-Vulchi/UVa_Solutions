n=int(input())
while (n != 0):
    px=input()
    py=input()
    while (n):
        x=input()
        y=input()
        if (x == px or y == py):
            print("divisa")
        elif (x < px and y > py):
            print("NO")
        elif (x > px and y > py):
            print("NE")
        elif (x > px and y < py):
            print("SE")
	else (x < px and y < py):
            print("SO")
	n-=1

	
