def Factorial(n):
    if n ==1:
        return 1
    return n * Factorial(n-1)


Factorial(4)
print(Factorial(5))