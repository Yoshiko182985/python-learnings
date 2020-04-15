#This is my Projects For Tamer python file! These are projects I've made with or for him.

#Future Tasks:
#1. Find the average of three user-given numbers!
#2. Make it optional to print the menu in the last function
#3. Make a function that allows any string to print any different color of text!
#---------------------------------------------------------------------------------------

#Print as many stars as the variable "count", make them all appear on the same line... Challenge: Maybe make it randomized or from user input?

def func1():
    starnum = int(input("How many stars would you like to print? "))

    for m in range (0, starnum):
        print("*", end = "" )
    print("\n")

#---------------------------------------------------------------------------------------

#This exercise runs a function that prints stars in a pyramid shape depending on user input

def printStars(numStars):
    m = 0
    while (m < numStars):
        print("*", end = "")
        m = m + 1
    print("")

def func2 ():
    size = int(input("Pyramid size: "))
    a = 1
    while (a <= size):
        printStars(a)
        a = a + 1

#---------------------------------------------------------------------------------------

#This file asks for your name and age and tells you whether or not you're allowed to drink!

def func3 ():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    print (name, "is", (age), "years old.")

    if age >= 21:
        print("You can drink!!!")
    else:
        print("Uh oh, you can't drink...")

#---------------------------------------------------------------------------------------

#Goes through my ages from 0-82, and for each age, prints my age and Tamer's age. It's basically a loop with a few if and elif statements tossed in!

def func4 ():
    for currentage in range (0, 83):
        if currentage < 19:
            print("When I was " + str(currentage) + ", Tamer was " + str(currentage + 18))
        elif currentage == 19:
            print("Now that I'm " + str(currentage) + ", Tamer is " + str(currentage + 18))
        elif currentage == 82:
            print("When I'm " + str(currentage) + ", Tamer will officially be " + str(currentage + 18) + " aka an old, old man. Happy future birthday to the most beloved geezer!")
        else:
             print("When I'm " + str(currentage) + ", Tamer will be " + str(currentage + 18))

#---------------------------------------------------------------------------------------

def pickMenu():
    choice = int(input("Which function would you like? "))

    if choice  == 1:
        func1()
    elif choice == 2:
        func2()
    elif choice == 3:
        func3()
    elif choice == 4:
        func4()
    elif choice == 5:
        exit()
    else:
        print("I'm sorry, your input is invalid. Please pick one of the numbers on the menu!")

def printMenu():
    print("\033[94mFunction Menu:\033[0m")
    print(" 1. Prints as many stars as you'd like")
    print(" 2. Prints the amount of stars you'd like as the bottom row of a pyramid")
    print(" 3. Tells you whether or not you're allowed to drink")
    print(" 4. Tells me what age Tamer and I will be at certain times")
    print(" 5. Exit this program")
    print("")

while (True):
    print()
    printMenu()
    pickMenu()

#---------------------------------------------------------------------------------------

