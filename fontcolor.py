#The goal of this program is to cree a function that can be implemented in other programs. The function will take input (a string) and output that string using shell colors in terminal

START = "\033["
END = "\033[0m"

colorDic = {
        "red" : "31m",
        "green" : "32m",
        "yellow" : "33m",
        "blue" : "34m",
        "magenta" : "35m",
        "teal" : "36m",
        "lightGrey" : "37m",
        "darkGrey" : "90m",
        "orange" : "91m",
        "lightGreen" : "92m",
        "lightYellow" : "93m",
        "lavender" : "94m",
        "pink" : "95m",
        "lightBlue" : "96m"
        }

def to(color, text):
    return(START + colorDic[color] + text + END)

#If I'd like to import this file into other ones for later use, please pay close attention to the following directions!
# 1. import fontcolor as col
#  ~ by adding "as col", we're importing fontcolor under a nickname, so we won't have to call the full file name every time!
# 2. print(col.to("pink", "Hi!"))
