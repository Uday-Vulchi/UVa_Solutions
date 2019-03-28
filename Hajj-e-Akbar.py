n = 1
while n:
    str = input()
    if str == '*':
        break
    if str == 'Hajj':
        print("Case %d: Hajj-e-Akbar"%n)
    elif str == 'Umrah':
        print("Case %d: Hajj-e-Asghar"%n)
    n = n+1
