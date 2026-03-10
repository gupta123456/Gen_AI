def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        return "Negative Number not allowed"
    else:
        return n * factorial(n - 1)

print(factorial(5))
print(factorial(0))
print(factorial(-3))