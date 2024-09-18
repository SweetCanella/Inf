def f(a):
    if a == 1 or a == 2:
        return 'yep'
    for i in range (2,int(a**0.5)+2):
        if a%i==0:
            return 'nope'
    return 'yep'

a = int(input())
print(f(a))