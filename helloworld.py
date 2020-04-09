print("Hello, world!")

print("\n")

#Variables are created upon declaration
#Strings can be declared with the use of double or single quotes
a =  '"Hey! '
b =  'John Doe!"'
print (a + b)

print("\n")

#Python allows you to assign values to multiple variables in one line!
e, f, g = "Orange", "Banana", "Cherry"
print (e)
print (f)
print (g)

print("\n")

#You can also assign the same value to multiple variables in one line!
h = i = j = "Apple"
print (h)
print (i)
print (j)

print("\n")

#If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value!
k = "awesome"

def func1():
    k = "fantastic"
    print("Python is " + k)

func1()

#The area inside a function's parentheses (argument) can also be given a variable whose meaning will be defined when the function is called
def func2(k):
    print("Python is " + k)

func2("cool")
func2("terrible")

print("\n")

#How to get random numbers
print("Let's generate some random numbers!")
import random
print (random.randrange(1,10))

print("\n")

l = """Remember how we made a multiline comment earlier? This is a multiline string variable using three quotes! It's the same as making a comment, but this time the variable will be called on!"""
print(l)

print ("\n")

#Strings are arrays! You can either call on one character, or you can call on a range of characters using the slice syntax. Just remember, counting arrays starts from zero, and when you slice, the last character isn't counted!
m = "Boots and cats"
print('The fourth character in "boots and cats" is ' + (m[4]))

print ('The slice of characters 4-8 in "boots and cats" is '+ (m[4:8]))

#You can also use negative indexes to start the slice from the end of the string!
print ('The negative index of characters 4-1 in "boots and cats" is ' + (m[-4:-1]))

#Let's count string length!
print ('"Boots and cats" has '+ str(len(m)) +' characters')

#Returns the string in all lowercase
print (m.lower())

#Returns the string in all uppercase
print (m.upper())

#Replaces a string with another string
print (m.replace("cats", "dogs"))

print ("\n")

#Checks if a phrase/character is present in a string using "in" or "not in", verified with true or false
txt = "The rain in Spain stays mainly in the plain"
n = "ain" in txt
print (n)

o = "ain" not in txt
print (o)

print ("\n")

#Let's merge variables!
p = "Bon"
q = "journee!"
r = p + " " + q
print (r)

print ("\n")

#The "format()" method taxes the passed arguments, formats them, and places them in the string where the placeholers {} are
age = 19
txt2 = "My name is Jo, and I'm {} years old!"
print(txt2.format(age))

print ("\n")

#"format()" taxes unlimited numbers of arguments whih are placed into their respective placeholders
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for ${}."
print (myorder.format(quantity, itemno, price))

print ("\n")

#To insert characters that are illegal in a string, use an escape character (\) followed by the character you want to insert
txt3 = "We are the so-called \"Vikings\" from the north!"
print (txt3)

print ("\n")

#Creates a new line (Carriage return)
#In python 2, the standard way of printing was without parentheses
txt4 = ("What goes,\nlet go")
print (txt4)

txt5 = ("Long time\tno see!")
print (txt5)

print ("\n")

#Let's take a look at string methods! They return new values but don't change the original string. Methods are called with yourvariable.methodname()
s = "I always like to fall asleep when it's raining."
print (s.casefold())

print ("\n")

#Lets review booleans!
print (10 > 9)
print (10 == 9)
print (10 < 9)

#Let's use booleans in if/then statements!
t = 200
u = 33

if u > t:
    print ("u is greater than t")
else:
    print ("u is not greater than t")

#You can execute code based on the boolean answer of a function EX: print yes if the function returns true, otherwise print no
def functhree() :
    return True

if functhree() :
    print("Yes")
else:
    print("No")

print ("\n")

#Let's work on some logical operators: and, or, and not

v = 5

print (v > 3 and v < 10)
print (v > 3 or  v < 4)
print (not(v > 3 and v < 10))

#Let's look into some identity operators: is, is not.
w = ["apple", "banana"]
x = ["apple", "banana"]
y = w

print ("\n")

#"==" compares for value, is compares for identity

print (w is y)
#Returns True because w is the same object as y

print (w is x)
#Returns False because w is not the same object as x, even if they have the same content

print (w == x)
#This demonstrates the difference between "is" and "==": this comparison returns True because w is equal to x

print ("\n")

#"in" returns True if a sequence with the specified value is present in the object
print ("banana" in w)
#Returns True because a sequence with the value "banana" is in the list

print ("pineapple" not in w)
#Returns True  because a sequence with the value "pineapple" is not in the list

print ("\n")

#A list is a collection which is ordered and changeable
list1 = ["apple", "banana", "cherry"]
print (list1)

#You access the list items by referring to the index number. Letps print the second item of the list!
print(list1[1])

#Let's try using a negative index, aka beginning from the end! -1 is the last item, -2 is the second to last item, etc...
print(list1[-1])

print ("\n")

#Let's practice specifying a range of indexes by specifying where to start and end the range. When specifying a range, the return value will be a new list with the specified items
list2 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list2[2:5])

#By leaving out the start value, the range will start at the first item
print(list2[:4])

#By leaving out the end value, the range will go on to the end of the list
print(list2[2:])

#Specify negative indexes if you want to start the search from the end of the list
print(list2[-4:-1])

print ("\n")

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

print ("\n")

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



print ("\n")

print ("\n")

print ("\n")
