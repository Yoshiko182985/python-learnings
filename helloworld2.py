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
    def helloPerson(self):
        print("Hello, my name is", self.fname, self.lname, "and I'm", str(self.age))

print()

#Let's learn how to create a child class, which inherits the functionality from another class and sets the parent class as a parameter when creating the child class
#Python has a super() function that will make the child lass inherit all the methods and properties from its parent
class Student(Person):
    def __init__(self, fname, lname, age, year):
        super().__init__(fname, lname, age)
        self.graduationyear = year

    def helloStudent(self):
        print("Hi! I'm", self.fname, self.lname, "and I graduated in year", str(self.graduationyear))

#This is an object
p1 = Person("Jo", "Burrell", 19)
p2 = Student("Maddy", "Burrell", 17, 2020)

#You can also modify properties on objects like this:
p1.age = 20

p1.helloPerson()
p2.helloStudent()

print()

#An iterator is an object that contains a countable number of values
#Iterators are objects that allow you to traverse a collectioni
#Technically, in python,an iterator is an object which implemenmts the next iterator protocol, which consist of the methods __iter__() and __next__()
happyThings = ("smiles", "kittens", "hugs")
happyIt = iter(happyThings)

print (next(happyIt))
print (next(happyIt))
print (next(happyIt))

print()

#Even strings are iterable objects and can return an iterator
myString = "poodle"
stringIt = iter(myString)

while True:
    try:
        s = next(stringIt)
        print (s.upper(), end="")
    except StopIteration:
        print()
        break

print()
#Now let's iterate through a tuple
#break always breaks out of loops!
list = ("qt", "lovely", "beautiful", "bb")
itr = iter(list)

while True:
    try:
        print(next(itr))
    except:
        break

#And here's a quick refresher on how to use "continue"
for i in range(0, 10):
    if (i == 2):
        continue
    print (i)
    print (i * i)

print("Jo is awesome")


#To create an object/class as an iterator, you have to implement the methods __iter__() and __next()__ to your object
#Let's create an iterator that returns numbers, starting with 1, and each sequence will increase by one
class myNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = myNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print()
#The example above would continue forever if we had enough next() statements, or if it was used in a for loop
#To provent the iteration from going on forever, we can use the StopIteration statement
#In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times
#Let's stop the next example after 20 iterationw
class myNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = myNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)

print()
#A variable is only available from inside the reigon it is created. This is called "scope"
#If you need to create a global variable but are stuck in the local scope, you can use the global keyword, which makes the variable global!
def myFunc():
    global x
    x = 300

myFunc()
print(x)

#Also use the global keyword if you want to make a change to a global variable inside a function!

y = 300

def myFunc2():
    global y
    y = 200

myFunc2()
print(y)

#Modules are like code libraries! They're files that contain sets of functions you want to include in your application
import helloworldmodule as hwm

hwm.greeting("Jo")

age = hwm.person1["age"]
print(age)

#There are several built in modules in python which you an import whenever you like
import platform
z = platform.system()
print(z)

#There's a built in function to list all the funtion list all the function names (or variable names) in a module. The dir() function:
m = dir(platform)
print(m)

#You can choose to import only parts from a module, by using the "from" keyword
from helloworldmodule import person2
print(person2["age"])

#A date in python is not a data type of its own, but we can import a module named datetime to work with dates as date objects
#Let's import the datetime module and display the current date
import datetime

n = datetime.datetime.now()
print(n)

#year
print(n.year)

#weekday
print(n.strftime("%A"))

#To create a date, we can use the datetime() class (constructor) of th datetime module.
#The datetime() class requires three parameters to create a date: year, month, day
o = datetime.datetime(2020, 5, 17)
print(o)

#The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone), but they're optional and have default values of 0
#The datetime object also has a method to format date objects into readable strings, called strftime(), and takes one parameter, format, to specify the format of the returned string
a = datetime.datetime(2018, 6, 1)
print(a.strftime("%B"))

#JSON is a syntax for storing and exchanging data. It's wtitten text, written with JavaScript object notation
#Python has a built in package called json which can be used to work with json data
import json

#if you habe a json string you can parse it by using the json.loads() method. the result will be a python dictionary
#some JSON:
X = '{ "name":"Johnathan", "age":27, "city":"San Jose"} '

#parse x
Y = json.loads(X)

#the result is a python dictionary
print(Y["age"])

#If you have a python object, you can convert it into a JSON string by using the json.dumps() method
#This is a python object(dictionary):
t = {
    "name": "Alex",
    "age": 30,
    "city": "San Jose"
}

#convert into JSON:
u = json.dumps(t)

#the result is a JSON string
print(u)

print(json.dumps({"name": "Maddy", "age":17, "city":"Hudsonville"}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

#Convert a python object containing all the legal data types
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x, indent=4, sort_keys=True))

#The try block lets you test a block of code for errors
#The except block lets you handle the error
#The finally block lets you execute code, regardless of the result of the try-and except blocks

#When an error occurs, or exception, as we call it, Python will normally stop and generate an error message
#These exceptions can be handled using the try statement
try:
    print(xxx)
except:
    print("An exception occured")

#Since the try clock raises an error, the except block will be executed
#Without the try block, the program will crash and raise an error
#You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error:
#Print one message if the try block raises a NameError and another for other errorsa
try:
    print(xxx)
except NameError:
    print("Variable xxx is not defined")
except:
    print("Something else went wrong")


#You can use the else keyword to define a block of code to be executed if no errors were raised
#In this example, the try block does not generate any error
try:
    print("Hello!")
except:
    print("Something went wrong...")
else:
    print("Nothing went wrong!")

#The finally block, if specified, will be executed regardless if the try block raises an error or not
try:
  print(xxx)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

#This can be useful to close objects and clean up resources
#Let's try to open and write to a file that isn't writable
try:
    f = open("demofile.txt")
    f.write("Some random text")
except:
    print("Something went wrong when writing to the file")
finally:
    f.close()

#As a python developer, you can choose to throw an exception if a condition occurs
#To throw (or raise) an exception, use the raise keyword
#Raise an error and stop the program if x is lower than 0
x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero!")

#The raise keyword is used to raise an exception
#You can define what kind of error to raise, and the text to print to the user
x = "hello"

if not type(x) is int:
    raise TypeError("Only integers are allowed!")
















