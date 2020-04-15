print("\033[94mHello, World!\033[0m")

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
replaceMe = "ain" in txt
print (replaceMe)

print ()

#The "format()" method takes the passed arguments, formats them, and places them in the string where the placeholers {} are
age = 19
myName = "My name is Jo, and I'm {} years old!"
print(myName.format(age))

print ()

#"format()" taxes unlimited numbers of arguments whih are placed into their respective placeholders
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for ${}."
print (myorder.format(quantity, itemno, price))

print ()

#To insert characters that are illegal in a string, use an escape character (\) followed by the character you want to insert
vikings = "We are the so-called \"Vikings\" from the north!"
print (vikings)

print ()

#Creates a new line
whatGoes = ("What goes,\nlet go")
print (whatGoes)

#Creats an indentation
longTime = ("Long time\tno see!")
print (longTime)

print ()

#Let's take a look at string methods! They return new values but don't change the original string. Methods are called with yourvariable.methodname()
rain = "I sleep when it rains."
print (rain.casefold())

print ()

#Lets review booleans!
print (10 > 9)
print (10 == 9)
print (10 < 9)

#You can execute code based on the boolean answer of a function EX: print yes if the function returns true, otherwise print no
def ToF() :
    return True

if ToF() :
    print("Yes")
else:
    print("No")

print ()

#Let's work on some logical operators: and, or, and not
replaceMe = 5

print (replaceMe > 3 and replaceMe < 10)
print (replaceMe > 3 or  replaceMe < 4)
print (not(replaceMe > 3 and replaceMe < 10))

#Let's look into some identity operators: is, is not.
ab = ["apple", "banana"]
ab2 = ["apple", "banana"]
copy = ab

print ()

print (ab is copy)
#Returns True because ab is the same object as copy

print (ab is ab2)
#Returns False because ab is not the same object as ab2, even if they have the same content

print (ab == ab2)
#This demonstrates the difference between "is" and "==": this comparison returns True because ab is equal to ab2

print ()

#"in" returns True if a sequence with the specified value is present in the object
print ("banana" in ab)
#Returns True because a sequence with the value "banana" is in the list

print ("pineapple" not in ab)
#Returns True  because a sequence with the value "pineapple" is not in the list

print ()

#A list is a collection which is ordered and changeable
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print (fruits)

#You access the list items by referring to the index number. Letps print the second item of the list!
print(fruits[1])

#Let's try using a negative index, aka beginning from the end! -1 is the last item, -2 is the second to last item, etc...
print(fruits[-1])

print ()

#Let's practice specifying a range of indexes by specifying where to start and end the range. When specifying a range, the return value will be a new list with the specified items
print(fruits[2:5])

#By leaving out the start value, the range will start at the first item
print(fruits[:4])

#By leaving out the end value, the range will go on to the end of the list
print(fruits[2:])

#Specify negative indexes if you want to start the search from the end of the list
print(fruits[-4:-1])

print ()

#To change the value of a specific item, refer to the index number, for example, this changes the second item
fruits[1] = "blackcurrant"
print(fruits)

#You can loop through the list items by using a for loop
for replaceMe in fruits:
    print(replaceMe)

#To determine if a specified item is present in a list, use the in keyword
#Let's check if "apple" is present in the list
if "apple" in fruits:
    print("Yes, 'apple' is in the fruits list")

#To determine how many items a list has, use the len() function
print(len(fruits))

#To add an item to the end of a list, use the append() method
fruits.append("orange")
print(fruits)

#To add an item at the specified index, use the insert() method
#Let's insert an item at the second position
fruits.insert(1, "grape")
print(fruits)

#There are several methods to remove items from a list...
#Remove() - removes the information! It no longer exists and can't be used
fruits.remove("apple")
print(fruits)

#Pop() - removes the specified index or the last item if the index isn't specified, information isn't deleted, just removed and can be called on later
fruits.pop()
print(fruits)

#Del - removes the specified index or delete the whole list
#del fruits
#The clear() method empties the list
#fruits.clear()

#Let's learn how to copy lists!
fruits2 = fruits.copy()
print(fruits2)

#You can also copy lists using the list() method
fruits2 = list(fruits)
print(fruits2)

# There are several ways to join or concentrate two or mosre lists in python.
#Let's use the + sign to join two lists!
blah = ["a", "b", "c"]
blah2 = [ 1, 2, 3]
blah = blah + blah2
print(blah)

print ()

#A tuple iis a collection which is ordered and unchanable. Tuples are written with parentheses. You can access their items, negative index them, specify ranges of indexes, loop, check for items, check length, and add the same way you would with a list! The differences will be listed below
#Although you can't change tuple values, you can convert it into a list, change the list, and convert the list back to a tuple.
carTuple = ("Mazda", "Volkswagon", "Honda")
carList = list(carTuple)
carList[1] = "kiwi"
carTuple = tuple(carList)

print(carTuple)

#You can create a tuple with one item, but you have to put a comma in after the item or Python won't recognize the variable
smolTuple = ("apple",)
print(type(smolTuple))

#A set is a collection which is unordered and unindexed. In python, sets are written with curly brackets.
candySet = {"Mounds", "Almond Joy", "Crunch"}
print(candySet)

#You can't access items by referring to an index, since sets are unordered, but you can loop through the set items using a for loop or ask if the value is present in the set by using "in"
#This loops through the set and prints the values
for replaceMe in candySet:
    print(replaceMe)

#This checks to see if there's an item present in the set
print("Butterfinger" in candySet)

#You can add items to a set, but can't change preexisting items
candySet.add("Hershey's Kiss")
print(candySet)

#Or even add multiple items at once using update()
candySet.update(["Snickers", "M&Ms", "Milka"])
print (candySet)

#To remove an item, use remove() or discard()
candySet.remove("Snickers")
print(candySet)

#There are two ways to join two or more sets in python. You can use union() or update()
agh = {"a", "b", "c"}
agh2 = {1, 2, 3}
agh.update(agh2)
print(agh)

print ()

#And FINALLY let's play around with if/else statements
dd = 200
cc = 33
if dd > cc:
    print("dd is greater than cc")
elif cc == dd:
    print("cc and dd are equal")
else:
    print("cc is greater than dd")

#You can have nested if statements
replaceMe = 41

if replaceMe > 10:
    print("Above ten,")
    if replaceMe > 20:
        print("and also above 20")
    else:
        print("but not above 20")

print ()

#Let's learn about while loops! While loops execute a set of statements as long as the condition is true
replaceMe = 1
while replaceMe < 6:
    print(replaceMe)
    replaceMe += 1

print ()

#With the "break" statement, we can stop the loop even if the while condition is true
replaceMe = 1
while replaceMe < 6:
    print(replaceMe)
    if (replaceMe == 3):
        break
    replaceMe += 1

print ()

#With the continue statement, we can stop the current iteration and continue to the next loop
replaceMe = 0
while replaceMe < 6:
    replaceMe += 1
    if replaceMe == 3:
        continue
    print(replaceMe)

print ()

#We can also use else statements once a block of code is no longer true
replaceMe = 1
while replaceMe < 6:
    print(replaceMe)
    replaceMe += 1
else:
    print("Variable is no longer less than six")

print ()

#For loops time! These things are used for iterating over a sequence (list, tuple, dictionary, set, or string). Using these, we can execufte a set of statements, once for each item in a list, tuple, set, etc...
for replaceMe in fruits:
    print(replaceMe)

for replaceMe in ("banana"):
    print(replaceMe)

#To loop through a set of code a specified number of times, we can use the range() function. It returns a sequene of numbers, starting from 0 and increments by one, and ends at a specified number
for replaceMe in range (6):
    print (replaceMe)

print ()

#Specifies the range of numbers to be cycled through
for replaceMe in range(2,6):
    print(replaceMe)

print ()

#Speifies the range of numbers to be cycled through and the increment that it'll increase by
for replaceMe in range (2, 30, 3):
    print(replaceMe)

#The else keyword in a for loop specifies a block of code to be executed when the loop is finished
for replaceMe in range(6):
    print(replaceMe)
else:
    print("Finally finished!")

#A nested loop is a loop inside a loop. The inner loop will be executed one time for each iteration of the outer loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for hh in adj:
    for ii in fruits:
        print (hh, ii)

# Let's learn about functions! A function is a block of code which only runs when it's called. You can pass data, known as parameters, into a function. Functions can return data as a result
#Arguments are specified after the function name inside the parentheses. You can add as many arguments as you'd like, just separate them with a comma.
def names(lastname):
    print(lastname + " Smith")

names ("John")
names ("Andy")
names ("Breanna")

#Functions must be called with the correct number of arguments, for example, if your function expects two arguments, you have to call the function with two arguments
def names2(fname, lname):
    print(fname + " " + lname)

names2("Sasha", "Brown")

#You can also send arguments with the key = value syntax... This way, the order doesn't matter!
def children(child3, child2, child1):
    print("The youngest child is " + child3)

children(child1 = "Josh", child2 = "Billy", child3 = "Tobias")

#This shows how to use a default parameter value, aka what happens if we call the function without an argument
def location(country = "Norway"):
    print("I am from " + country)

location("Sweden")
location("India")
location()
location("Brazil")

#To let a function return a value, use the "return" statement
def x(replaceMe):
    return 5 * replaceMe

print(x(3))
print(x(5))
print(x(9))

print ()

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

#Let's learn about dictionaries!
#Dictionaries are unordered, changable, indexed, collections. They're written with curly brackets and invlude keys and values.
thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
        }
print(thisdict)
#you can access the items of a dictionary by referring to it's key name, inside square brakets
xx = thisdict["model"]
#you can also use the method get()
yy = thisdict.get("model")

#You can hange the value of a specific item by referring to it's key name
thisdict["year"] = 2018

#You an loop through a dictionary by using a "for" loop. when looping through a dictionary, the return values are the keys of the dictionary, but there are methods to return the values as well
for zz in thisdict:
    print(zz)
#now let's print all the values in the dictionary, one by one
for zz in thisdict:
    print(thisdict[zz])
#or you an loop through both keys and values by using the items() function
for aaa, bbb in thisdict.items():
    print(aaa, bbb)

print(len(thisdict))

#adding an item to the dictionary is done by using a new index key and assigning a value to it
thisdict["color"] = "red"
print(thisdict)

