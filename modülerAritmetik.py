def bigintmodrecursion(a, b, mod):
    if b == 1:
        return a % mod

    new_a = (a * a) % mod
    new_b = b // 2
    result = bigintmodrecursion(new_a, new_b, mod)

    if b % 2 == 0:
        return result % mod
    else:
        return (result * a) % mod


a, b, c = map(int, input().split())
result = bigintmodrecursion(a, b, c)
print("result = ", result)
