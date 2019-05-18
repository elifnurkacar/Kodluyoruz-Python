


def findFibonaccci(x):
    a=1
    b=1
    list = [a]
    while b < x:
        list.append(b)
        a, b = b, a + b
    return list
x = 60
print(findFibonaccci(x))