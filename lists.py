myList = [1, 2, 3, 4, 5]

# Prints the list of numbers from the third index (Index starts from 0)
# Result: [4, 5]
print(myList[3:])

# Prints every alternate number from the list
# Result: [1, 3, 5]
print(myList[::2])

# Prints numbers from 0 to 99
for i in range(100):
    print(i)

myList = list(range(100))

# Prints every other 10th number in the sequence
# Result: 0, 10, 20, ..., 80, 90
print(myList[::10])

# Reverses the list and prints every other 10th number in the sequence
# Result: 99, 89, ..., 19, 9
print(myList[::-10])

# Append adds the new number to the end of the list
# Result: [1, 2, 3, 4, 5]
myList = [1, 2, 3, 4]
myList.append(5)
print(myList)

# Insert adds the new number to the specified position (or index) in the list
# Result: [1, 2, 3, 'a new val', 4, 5]
myList.insert(3, 'a new val')
print(myList)

# Pop removes the last element from the list
# Result: 4
myList = [1, 2, 3, 4]
print(myList.pop())

# Prints the list in reverse order and the list at the end is an empty list
while len(myList):
    print(myList.pop())

# Shallow copying of lists
# Both the lists get modified as they point towards the same memory location
# Result:
# [1, 2, 3, 4] - list a
# [1, 2, 3, 4] - list b
a = [1, 2, 3]
b = a;
a.append(4)
print(a)
print(b)

# Deep copy using copy() method
# Result:
# [1, 2, 3, 4, 5, 6] - list a
# [1, 2, 3, 4, 5] - list b
a = [1, 2, 3, 4, 5]
b = a.copy()
a.append(6)
print(a)
print(b)