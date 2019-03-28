k = int(input())
for i in range(1,k+1):
    s = list(map(int,input().split()))
    s.sort()
    s.reverse()
    print('Case %d:' %i ,s[0])
