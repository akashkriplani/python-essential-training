# Lambda functions

# Inline functions with implicit return

print((lambda x: x + 3)(5))

# Sort the list using sorted method inbuilt from python
myList = [5, 3, 4, 1, 2]
print(sorted(myList))

# Sort the list of dictionaries using lambda functions and sorted methd
myList = [{ 'num': 4 }, { 'num': 2 }, { 'num': 3 }]
print(sorted(myList, key=lambda x: x['num']))