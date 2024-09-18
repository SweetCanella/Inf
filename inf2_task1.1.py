def f(a,n):
    x=0
    a = str(a)
    k = -1
    s=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L''M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for i in range(len(a)):
        x = x + s.index(a[k])*n**i
        k -= 1
    return x

n = int(input())
a = input()
print(f(a,n))