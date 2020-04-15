#This is part 2 of helloworld!

#This is a class
#Use the __init__() function to assign values to object properties or other operations that are necessary to do when the objet is being created
#The self parameter is a reference to the current instance of the class, and is used to acess variales that belong to the class
class Person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

#Objects can also contain methods (functions that belong to the object)
    def hello(this):
        print("Hello, my name is", this.fname, this.lname, "and I'm", str(this.age))

#Let's learn how to create a child class, which inherits the functionality from another class and sets the parent class as a parameter when creating the child class
class Student(Person):
    pass


#This is an object
p1 = Person("Jo", "Burrell", 19)

#You can also modify properties on objects like this:
p1.age = 20

p1.hello()

