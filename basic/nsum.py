def sum(n):
    if n == 0:
        return 0
    return n + sum(n - 1)

print("Sum of first 5 natural numbers is", sum(3))