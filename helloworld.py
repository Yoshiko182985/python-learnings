print("Hello, world!")

#This is a comment!

print("The weather today is quite nice.")
#print("Although I've heard it might rain soon...")

print("\n")

"""
This a "multiline comment". It's less highly recommended because it's actually not a comment! Technically, it's a multiline string. Python ignores string literals (text constants) that aren't assigned to a variable. It's not displayed, but exists and could potentially cause unexpected errors, so it's still recommended to use regular hashtags in comments!
"""

#Variables are created upon declaration
#Strings can be declared with the use of double or single quotes
a =  '"Hey! '
b =  'John Doe!"'
print (a + b)

print("\n")

#Python allows you to assign values to multiple variales in one line!
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

def funcone():
    k = "fantastic"
    print("Python is " + k)

funcone()

#The area inside a function's parentheses (argument) can also be given a variable whose meaning will be defined when the function is called

def functwo(k):
    print("Python is " + k)

functwo("cool")
functwo("terrible")

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
txt_2 = "My name is Jo, and I'm {} years old!"
print(txt_2.format(age))

print ("\n")

#"format()" taxes unlimited numbers of arguments whih are placed into their respective placeholders
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for ${}."
print (myorder.format(quantity, itemno, price))

print ("\n")

#To insert characters that are illegal in a string, use an escape character (\) followed by the character you want to insert
txt_3 = "We are the so-called \"Vikings\" from the north!"
print (txt_3)

print ("\n")

#Creates a new line (Carriage return)
#In python 2, the standard way of printing was without parentheses
txt_4 = ("What goes,\nlet go")
print (txt_4)

txt_5 = ("Long time\tno see!")
print (txt_5)

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




print("Bye felisha")



print ("\n")

