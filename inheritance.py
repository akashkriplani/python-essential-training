# Class Inheritance

# Parent Class
class Dog:
    _legs = 4

    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + ' says: Bark!')

    def getLegs(self):
        return self._legs

# Child Class
class Chihuahua(Dog):
    # Parent class speak method overridden in child class
    def speak(self):
        print(f'{self.name} says: Yap Yap Yap!')

    def wagTail(self):
        print('Vigourous Wagging')

dog = Chihuahua('Roxy')
print(dog.speak())
print(dog.wagTail())

myDog = Dog('Rover')
print(myDog.speak())

# Extending Built-in Classes

# Extend a built-in append method from list to return the list of unique items
class UniqueList(list):
    def __init__(self):
        super().__init__(self)
        self.someProperty = 'Unique List!'

    def append(self, item):
        if item in self:
            return
        super().append(item)

uniqueList = UniqueList()

uniqueList.append(1)
uniqueList.append(1)
uniqueList.append(2)
uniqueList.append(2)
uniqueList.append(2)
uniqueList.append(3)

print(uniqueList)
print(uniqueList.someProperty)
