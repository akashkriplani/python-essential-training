# Factorial Challenge
# The factorial function gives the number of possible arrangements of a set of items of length "n"

# For example, there are 4! ("four factorial") or 24 ways to arrange four items, which can be calculated as: 4 * 3 * 2 * 1

# 5! = 5 * 4 * 3 * 2 * 1 = 120

# 6! = 6 * 5 * 4 * 3 * 2 * 1 = 720

# etc.

# In a set of 0 items (an empty set) there is only one way to arrange the items, therefore, 0! = 1

# For the purposes of this exercise, factorials are only defined for positive integers (including 0)

# Returns the value of the factorial of n if it is defined, otherwise, returns None
def factorial(n):
    if type(n) is not int or n < 0:
        return None
    
    if n == 0 or n == 1:
        return 1
    
    return n * factorial (n - 1)

# 1
print(factorial(0))
# 1
print(factorial(1))
# None
print(factorial(1.43))
# None
print(factorial(-1.7))
# 120
print(factorial(5))
# 720
print(factorial(6))
# 3628800
print(factorial(10))
