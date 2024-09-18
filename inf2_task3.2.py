def f(a):
    return int(((1+a)/2)*a)

a = int(input())
x = 0
for i in range(1,a+1):
    x = x+i
print('циклом',x)
print('без цикла',f(a))
