print("\033[94mHello, World!\033[0m")

print()

#You can assign values to multiple variables at a time!
a, b, c  = "Apple", "Banana", "Cherry"
print (a)
print (b)
print (c)

print()

#You can also assign the same value to multiple variables in one line!
d1 = d2 = d3 = "Dragonfruit"
print (d1)
print (d2)
print (d3)

print()

#If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value!
adj = "awesome"

def pythonIs():
    adj = "fantastic"
    print("Python is " + adj)

pythonIs()

#The area inside a function's parentheses (argument) can also be given a variable whose meaning will be defined when the function is called
def pythonIs2(adj2):
    print("Python is " + adj2)

pythonIs2("cool")
pythonIs2("terrible")

print()

#How to get random numbers
print("Let's generate some random numbers!")
import random
print (random.randrange(1,10))

print()

#Strings are arrays! You can either call on one character, or you can call on a range of characters using the slice syntax. Just remember, counting arrays starts from zero, and when you slice, the last character isn't counted!
BAC = "Boots and cats"
print('The fourth character in "boots and cats" is ' + (BAC[4]))

print ('The slice of characters 4-8 in "boots and cats" is '+ (BAC[4:8]))

#You can also use negative indexes to start the slice from the end of the string!
print ('The negative index of characters 4-1 in "boots and cats" is ' + (BAC[-4:-1]))

#Let's count string length!
print ('"Boots and cats" has '+ str(len(BAC)) +' characters')

#Returns the string in all lowercase
print (BAC.lower())

#Returns the string in all uppercase
print (BAC.upper())

#Replaces a string with another string
print (BAC.replace("cats", "dogs"))

print ()

#Checks if a phrase/character is present in a string using "in" or "not in", verified with true or false
txt = "The rain in Spain stays mainly in the plain"
e = "ain" in txt
print (e)

f = "ain" not in txt
print (f)

print ()

#The "format()" method takes the passed arguments, formats them, and places them in the string where the placeholers {} are
age = 19
txt2 = "My name is Jo, and I'm {} years old!"
print(txt2.format(age))

print ()

#"format()" taxes unlimited numbers of arguments whih are placed into their respective placeholders
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for ${}."
print (myorder.format(quantity, itemno, price))

print ()

#To insert characters that are illegal in a string, use an escape character (\) followed by the character you want to insert
txt3 = "We are the so-called \"Vikings\" from the north!"
print (txt3)

print ()

#Creates a new line
txt4 = ("What goes,\nlet go")
print (txt4)

#Creats an indentation
txt5 = ("Long time\tno see!")
print (txt5)

print ()

#Let's take a look at string methods! They return new values but don't change the original string. Methods are called with yourvariable.methodname()
rain = "I sleep when it rains."
print (rain.casefold())

print ()

#Lets review booleans!
print (10 > 9)
print (10 == 9)
print (10 < 9)

#Let's use booleans in if/then statements!
th = 200
tt = 33

if th > tt:
    print ("th is greater than tt")
else:
    print ("tt is not greater than th")

#You can execute code based on the boolean answer of a function EX: print yes if the function returns true, otherwise print no
def ToF() :
    return True

if ToF() :
    print("Yes")
else:
    print("No")

print ()

#Let's work on some logical operators: and, or, and not
var = 5

print (var > 3 and var < 10)
print (var > 3 or  var < 4)
print (not(var > 3 and var < 10))

#Let's look into some identity operators: is, is not.
w = ["apple", "banana"]
x = ["apple", "banana"]
y = w

print ()

print (w is y)
#Returns True because w is the same object as y

print (w is x)
#Returns False because w is not the same object as x, even if they have the same content

print (w == x)
#This demonstrates the difference between "is" and "==": this comparison returns True because w is equal to x

print ()

#"in" returns True if a sequence with the specified value is present in the object
print ("banana" in w)
#Returns True because a sequence with the value "banana" is in the list

print ("pineapple" not in w)
#Returns True  because a sequence with the value "pineapple" is not in the list

print ()

#A list is a collection which is ordered and changeable
list1 = ["apple", "banana", "cherry"]
print (list1)

#You access the list items by referring to the index number. Letps print the second item of the list!
print(list1[1])

#Let's try using a negative index, aka beginning from the end! -1 is the last item, -2 is the second to last item, etc...
print(list1[-1])

print ()

#Let's practice specifying a range of indexes by specifying where to start and end the range. When specifying a range, the return value will be a new list with the specified items
list2 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list2[2:5])

#By leaving out the start value, the range will start at the first item
print(list2[:4])

#By leaving out the end value, the range will go on to the end of the list
print(list2[2:])

#Specify negative indexes if you want to start the search from the end of the list
print(list2[-4:-1])

print ()

#To change the value of a specific item, refer to the index number, for example, this changes the second item
list1[1] = "blackcurrant"
print(list1)

#You can loop through the list items by using a for loop
for z in list1:
    print(z)

#To determine if a specified item is present in a list, use the in keyword
#Let's check if "apple" is present in the list
if "apple" in list1:
    print("Yes, 'apple' is in the fruits list")

#To determine how many items a list has, use the len() function
print(len(list2))

#To add an item to the end of a list, use the append() method
list1.append("orange")
print(list1)

#To add an item at the specified index, use the insert() method
#Let's insert an item at the second position
list1.insert(1, "grape")
print(list1)

#There are several methods to remove items from a list...
#Remove() - removes the information! It no longer exists and can't be used
list1.remove("apple")
print(list1)

#Pop() - removes the specified index or the last item if the index isn't specified, information isn't deleted, just removed and can be called on later
list1.pop()
print(list1)

#Del - removes the specified index or delete the whole list
del list1[0]
print(list1)

del list1

#The clear() method empties the list
list3 = ["apple", "banana", "cherry"]
list3.clear()
print(list3)

#Let's learn how to copy lists!
list4 = list2.copy()
print(list4)

#You can also copy lists using the list() method
list5 = list(list2)
print(list5)

# There are several ways to join or concentrate two or mosre lists in python.
#Let's use the + sign to join two lists!
list6 = ["a", "b", "c"]
list7 = [ 1, 2, 3]
list8 = list6 + list7
print(list8)

#You can also append all the items from list7 into list6, one by one
for aa in list7:
    list6.append(aa)

print(list6)

#You can even use the extend() method, which adds elements from one list to another list

list7 = ["a", "b", "c"]
list8 = [1, 2, 3]

list7.extend(list8)
print(list7)

print ()

#A tuple is a collection which is ordered and unchanable. Tuples are written with parentheses. You can access their items, negative index them, specify ranges of indexes, loop, check for items, check length, and add the same way you would with a list! The differences will be listed below
#Although you can't change tuple values, you can convert it into a list, change the list, and convert the list back to a tuple.
tuple1 = ("apple", "banana", "cherry")
list8 = list(tuple1)
list8[1] = "kiwi"
tuple1 = tuple(list8)

print(tuple1)

#You can create a tuple with one item, but you have to put a comma in after the item or Python won't recognize the variable
tuple2 = ("apple",)
print(type(tuple2))

#A set is a collection which is unordered and unindexed. In python, sets are written with curly brackets.
set1 = {"apple", "banana", "cherry"}
print(set1)

#You can't access items by referring to an index, since sets are unordered, but you can loop through the set items using a for loop or ask if the value is present in the set by using "in"
#This loops through the set and prints the values
for bb in set1:
    print(bb)

#This checks to see if there's an item present in the set
print("banana" in set1)

#You can add items to a set, but can't change preexisting items
set1.add("orange")
print(set1)

#Or even add multiple items at once using update()
set1.update(["orange", "mango", "grape"])
print (set1)

#To remove an item, use remove() or discard()
set1.remove("banana")
print(set1)

#There are two ways to join two or more sets in python. You can use union() or update()
set2 = {"a", "b", "c"}
set3 = {1, 2, 3}
set2.update(set3)
print(set2)

print ("\n")

#And FINALLY let's play around with if/else statements
cc = 200
dd = 33
if dd > cc:
    print("dd is greater than cc")
elif cc == dd:
    print("cc and dd are equal")
else:
    print("cc is greater than dd")

#You can have nested if statements
ee = 41

if ee > 10:
    print("Above ten,")
    if ee > 20:
        print("and also above 20")
    else:
        print("but not above 20")

print ("\n")

#If statements can't be empty, but if you have an if statement without content, put in the pass statement to avoid getting an error
if cc > dd:
    pass

#Let's learn about while loops! While loops execute a set of statements as long as the condition is true
ff = 1
while ff < 6:
    print(ff)
    ff += 1

print ("\n")

#With the "break" statement, we can stop the loop even if the while condition is true
ff = 1
while ff < 6:
    print(ff)
    if (ff == 3):
        break
    ff += 1

print ("\n")

#With the continue statement, we can stop the current iteration and continue to the next loop
ff = 0
while ff < 6:
    ff += 1
    if ff == 3:
        continue
    print(ff)

print ("\n")

#We can also use else statements once a block of code is no longer true
ff = 1
while ff < 6:
    print(ff)
    ff += 1
else:
    print("ff is no longer less than six")

print ("\n")

#For loops time! These things are used for iterating over a sequence (list, tuple, dictionary, set, or string). Using these, we can execufte a set of statements, once for each item in a list, tuple, set, etc...
for gg in list2:
    print(gg)

for gg in ("banana"):
    print(gg)

#To loop through a set o code a specified number of times, we can use the range() function. It returns a sequene of numbers, starting from 0 and increments by one, and ends at a specified number
for gg in range (6):
    print (gg)

print ("\n")

#Specifies the range of numbers to be cycled through
for gg in range(2,6):
    print(gg)

print ("\n")

#Speifies the range of numbers to be cycled through and the increment that it'll increase by
for gg in range (2, 30, 3):
    print(gg)

#The else keyword in a for loop specifies a block of code to be executed when the loop is finished
for gg in range(6):
    print(gg)
else:
    print("Finally finished!")

#A nested loop is a loop inside a loop. The inner loop will be executed one time for each iteration of the outer loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for hh in adj:
    for ii in fruits:
        print (hh, ii)

# Let's learn about functions! A function is a block of code which only runs when it's called. You can pass data, known as parameters, into a function. Functions can return data as a result
def func1():
    print("Hello from a function!")

#Now let's call the function using the name followd by parenthesis
func1()

#Arguments are specified after the function name inside the parentheses. You can add as many arguments as you'd like, just separate them with a comma.
def func2(lastname):
    print(lastname + " Smith")

func2 ("John")
func2 ("Andy")
func2 ("Breanna")

#Functions must be called with the correct number of arguments, for example, if your function expects two arguments, you have to call the function with two arguments
def func3(fname, lname):
    print(fname + " " + lname)

func3("Sasha", "Brown")

#You can also send arguments with the key = value syntax... This way, the order doesn't matter!
def func4(child3, child2, child1):
    print("The youngest child is " + child3)

func4(child1 = "Josh", child2 = "Billy", child3 = "Tobias")

#This shows how to use a default parameter value, aka what happens if we call the function without an argument
def func5(country = "Norway"):
    print("I am from " + country)

func5("Sweden")
func5("India")
func5()
func5("Brazil")

#You can send any data types of argument to a function (string, number, list, disctionary, etc...) and it will be treated as the same data type inside the function
def func6(food):
    for jj in food:
        print(jj)

fruits = ["apple", "banana", "cherry"]
func6(fruits)

#To let a function return a value, use the "return" statement
def func7(kk):
    return 5 * kk

print(func7(3))
print(func7(5))
print(func7(9))

print ("\n")

#Let's learn about reursion! Recursion is a function that can call itself. This splits up the workload and keeps the computer focused on only the next task in front of itself

#Now let's take a look at this example. Remember factorials? The actual definition is "the product of an integer and all the integers below it. For example, this is what factorial 5 would look like...
#5! = 5 + 4 + 3 + 2 + 1 = 15
#In our example, we have 5! -> return 5 + 4! -> return 4 + 3! -> return 3 + 2! -> return 2 + 1!
#Now let's work backwards. 1! = 1, now add this to return 2 to get a product of 3. Now we have 2!, which we've determined is three, and when you add this to return 3, you'll get 6. Add six (aka, 3!) to return 4 to get 10. Finally, take your ten (4!), and add it to your original five! The total is fifteen.

print("Recursion Example Results")

def factorial(ll):
    if (ll == 0):
        result = 0
    else:
        result = ll + factorial(ll - 1)
        print("\t",  result)
    return result

#Or we can avoid the variable "result" and return the value as soon as either "if" or "else" is called
def fact(ll):
    if (ll == 0):
        return 0
    else:
        return ll + factorial(ll - 1)

res = factorial(5)
print(res)

print ()

#Let's make classes (templates) and objects (instances of it)
#note: self refers to the current instance of person, in other language, it's known as "this"
#a function that is part of an object is usually referred to as a method
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def func8(self):
        print("Hello, my name is " + self.name)

p1 = person("Jo", 19)

print(p1.name)
print(p1.age)
p1.func8()

#You can also modify properties on objects
p1.age = 25
print(p1.age)
#You can also delete objects by using the "del" keyword

print()

#Let's study python inheritance! This allows us to define a class that inserts all the methods and properties from another class
#There are two types: parent and child classes. The parent class is the class that's inhereted from, also called the base class. The child class is what inherets from another class, also called the derived class.
#Let's start by creating a new parent class!
class Cookies:
    def __init__(self, size):
        self.size = size

    def printCookies(self):
        print("The size of this cookie is " + self.size)

cookie1 = Cookies("Large")

cookie1.printCookies()








