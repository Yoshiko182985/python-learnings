# Let's learn file handling! In this file, we'll be learning to read, write, and
# delete from other files!

import sys
sys.path.append('../')
import fontcolor as col

#This opens and reads all of demofile.txt
f = open("demofile.txt", "r")
print(col.to("red", f.read()))

#This specifies to return the first five characters of the file
f = open("demofile.txt", "r")
print(col.to("orange", f.read(5)))

#You can return one line y using the readline() method
f = open("demofile.txt", "r")
print(col.to("lightYellow", f.readline()))

#Or read two lines by callin readline() twice!
f = open("demofile.txt", "r")
print(col.to("yellow", f.readline()))
print(col.to("yellow", f.readline()))

#By looping through the lines of the file, you can read the whole file, line by line
f = open("demofile.txt", "r")
for m in f:
    print(col.to("lightGreen", (m)))

#Let's add some content to this file!
f = open("demofile.txt", "a")
f.write("This is a line that will be written in! ")

f.close()

f = open("demofile.txt", "r")
print(f.read())

