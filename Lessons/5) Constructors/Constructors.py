class Animal(object):
    def __init__(self, name, age): #Initializer methodu.
        self.name = name
        self.age = age

    def getAge(self):
        return self.age

    def getName(self):
        return self.name

a1 = Animal("dog", 2)
a1Age = a1.getAge()
a1Name = a1.getName()
print("Animal Name: ", a1Name)
print("Animal Age: ", a1Age)