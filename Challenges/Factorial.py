# Find the factorial of a given number

def factorial(n):
    if type(n) is not int or n < 0:
        return None
    
    if n == 0 or n == 1:
        return 1
    
    return n * factorial (n - 1)

print(factorial(0))
print(factorial(1))
print(factorial(1.43))
print(factorial(-1.7))
print(factorial(5))
print(factorial(6))
print(factorial(10))
