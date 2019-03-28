def s_e(a,b):
    if b==1:
        return a
    else:
        return s_e(a,b-1)*a
n,m=map(int,input().split())
print(s_e(n,m))
