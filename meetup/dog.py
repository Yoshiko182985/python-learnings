class Person:
    def __init__(self, name):
        self.name = name

class Dog:
    # constructor takes string and Person
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner

    def bark(self):
        print(self.name, "says WOOF to", self.owner.name)

tamii = Person("Tamii")
print(type(tamii))

olix = Dog("Olix", tamii)
print(type(olix))
print(type("tamii"))
olix.bark()
