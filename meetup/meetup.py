#The purpose of this program is to divide Meetup attendees into groups for me!
#This is how many people you have signed up!
#This is how many native speakers you have!
#How many people would you like in each group?
#Native speakers top priority is 3, 2, 1, 0
#Add in a switch function for moving members around
#Every time members are moved, print the current lists
#Name groups!

# This class represents a Level
# It has id (int) and name (String)
# constructor 2 args
# a description() method
class Level:
    def __init__(self, id, name, prettyName):
        self.id = id
        self.name = name
        self.prettyName = prettyName

    def description(self):
        return self.prettyName + ' (' + self.name + ') ID ' + str(self.id)

# This class represents a Member
# It has a name (String) and a level (Level)
class Member:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def description(self):
        return self.name + ", " + self.level.prettyName

# This reads levels from the config file
# and returns a dictionary where the key is
# id and the value is a Level object
#1. read file line by line
#2. split the line into three pieces
#3. make a Level (0bject) using those values
#4. put in dictionary
#5. return
def loadLevels(filename):
    o = open("levels.conf", "r")
    levels = {}

    for everyLine in o:
        array = everyLine.split(", ")
        array[2] = array[2].strip()
        level = Level(array[1], array[0], array[2])
        levels[array[1]] = level
    o.close()
    return levels

# This reads members from the other config
# file and returns
# Making a function to load members.
# Return a list instead of dictionary. That's literally the only difference from the other five steps last time :)
def loadMembers(filename, levels):
    o = open("members.conf", "r")
    members = []

    for everyLine in o:
        array = everyLine.split(", ")
        array[1] = array[1].strip()
        member = Member(array[0], array[1])
        members.append(array[0])
    o.close()
    return members

levels = loadLevels('levels.conf') # dict of int -> Level
members = loadMembers('members.conf', levels)

for key in levels:
    print(levels[key].prettyName)


#member = Member("Bob", example)
#print(member.descriptgtion())
