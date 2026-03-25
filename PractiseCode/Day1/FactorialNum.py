import math

n = 6
print(math.factorial(n))


# Common Method
def fact(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    return 1 if n < 1 else n * fact(n - 1)


print(fact(6))
