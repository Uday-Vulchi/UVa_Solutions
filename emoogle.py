count = 0
def emoogle(n):
    global count
    summ = 0
    if n == 0:
        return  0
    else:
        A = list(map(int, input().split()))
        cnt += 1
        for i in range(len(A)):
            if A[i] > 0:
                summ += 1
            else:
                summ -= 1

        print("Case %d: %d"%(count,summ))
while True:
    n = int(input())
    if n == 0:
        break
    else:
        emoogle(n)
