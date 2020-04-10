#This is my Projects For Tamer python file! These are projects I've made with or for him.

#Future Tasks:
#Find the average of three user-given numbers!
#Add several print statements to each other without creating a new line
#Print as many stars as the variable "count", make them all appear on the same line... Challenge: Maybe make it randomized or from user input?
#Figure out how to choose which program to execute. Ask for user input and make sure it answers it correctly!

#----------------------------------------------------------------------------------------------

#Print as many stars as the variable "count", make them all appear on the same line... Challenge: Maybe make it randomized or from user input?
starnum = int(input("How many stars would you like to print? "))

for m in range (0, starnum):
    print("*", end = "" )

print("\n")

#----------------------------------------------------------------------------------------------

#This exercise runs a function that prints stars in a pyramid shape depending on user input
def printStars(numStars):
    m = 0
    while (m < numStars):
        print("*", end = "")
        m = m + 1
    print("")

size = int(input("Pyramid size: "))
a = 1

while (a <= size):
    printStars(a)
    a = a + 1

#----------------------------------------------------------------------------------------------

#This file asks for your name and age and tells you whether or not you're allowed to drink!
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print (name, "is", (age), "years old.")
#Plus signs were all that was available pre-python3, and you needed to include spaces in strings, but commas are a new feature in python3 that automatically adds in spaces! Oh the convenience of modern technology

if age >= 21:
    print("You can drink!!!")
else:
    print("Uh oh, you can't drink...")

print("")
#---------------------------------------------------------------------------------------------

#Goes through my ages from 0-82, and for each age, prints my age and Tamer's age. It's basically a loop with a few if and elif statements tossed in!
for currentage in range (0, 83):
    if currentage < 19:
        print("When I was " + str(currentage) + ", Tamer was " + str(currentage + 18))
    elif currentage == 19:
        print("Now that I'm " + str(currentage) + ", Tamer is " + str(currentage + 18))
    elif currentage == 82:
        print("When I'm " + str(currentage) + ", Tamer will  officially be " + str(currentage + 18) + " aka an old, old man. Happy future birthday to the most beloved geezer!")
    else:
         print("When I'm " + str(currentage) + ", Tamer will be " + str(currentage + 18))

print("")
#----------------------------------------------------------------------------------------------
