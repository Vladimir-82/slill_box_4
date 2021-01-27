def recursion(n):
    if n == 1:
        return 1
    else:
        recursion_minus_1 = recursion(n = n - 1)
        return recursion_minus_1 * n

print(recursion(3))