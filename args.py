#This file takes two arguments from terminal! The first is the file name, aka "num_stars), and the second is the number of stars! In this program, we import the arguments from terminal and use the input to interact with the content of our python file!
import sys
print(sys.argv)

if len(sys.argv) == 2:
    for i in range(0, int(sys.argv[1])):
        print("*", end = "")
    print()
else:
    print("Usage:", sys.argv[0], "num_stars")
