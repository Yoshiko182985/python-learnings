#This is my Projects For Tamer python file! These are projects I've made with or for him.

#Future Tasks:
#Find the average of three user-given numbers!
#Add several print statements to each other without creating a new line

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

#----------------------------------------------------------------------------------------------

#This file asks for your name and age and tells you whether or not you're allowed to drink!
age = int(input("Enter your age: "))
name = input("Enter your name: ")

print (name, "is", (age), "years old.")
#Plus signs were all that was available pre-python3, and you needed to include spaces in strings, but commas are a new feature in python3 that automatically adds in spaces! Oh the convenienes of modern technology

if age >= 21:
    print("You can drink!!!")
else:
    print("Uh oh, you can't drink...")


