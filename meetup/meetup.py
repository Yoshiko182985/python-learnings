# The purpose of this program is to divide Meetup attendees into groups for me!

# This class represents a Level
# It has id (int) and name (String)
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
        id = array[1]
        name = array[0]
        prettyName = array[2].strip()
        foo = Level(id, name, prettyName)
        levels[id] = foo
    o.close()
    return levels

# This reads members from the other config file
# The only difference between the two is that
# loadMembers returns a list instead of a
# dictionary, the other 5 steps are the same
def loadMembers(filename, levels):
    o = open("members.conf", "r")
    members = []

    for everyLine in o:
        array = everyLine.split(", ")
        name = array[0]
        levelId = array[1].strip()
        member = Member(name, levels[levelId])
        members.append(member)
    o.close()
    return members

levels = loadLevels('levels.conf')
weirdos = loadMembers('members.conf', levels)

print("LEVELS")
for key in levels:
    print(levels[key].prettyName)

print()
print("MEMBERS")
for m in weirdos:
    print(m.name, '(' + m.level.name + ')')

print()

print("NATIVES")
for m in weirdos:
    if (m.level.id) == "4":
        print(m.name)

print()
print("These are all the level ID's:")
for level in levels:
    print(level)

print()

# Iterates over levels, goes through members,
# and prints the names of all the people in
# that level
# In case Tamer quizzes me:
# levels is a dictionary, l is the key!
for l in levels:
    print(levels[l].prettyName + ":")

    for m in weirdos:

        if (m.level.id) == l:
            print(m.name)

    print()
