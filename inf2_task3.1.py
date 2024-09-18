def f(a):
    for i in range(2,a+1):
        if a%i == 0:
            return i
a = int(input())
print(f(a))