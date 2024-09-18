def f(a,n):
    s = ''
    while a>0:
        s = str(a%n) + s
        a = a//n
    return s

a = int(input())
n = int(input())
print(f(a,n))