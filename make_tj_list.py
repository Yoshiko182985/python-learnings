#This is a program that prints out JavaScript. It has a "dynamic" array of things I want to do with Tamer!
#So, you might be wondering, "How the hell do I execute my wonderful dynamic python-html hybrid?"
#1. Type this in Terminal: python3 make_tj_list.py > tj.html
#  ~ this redirects the output of this file to a html file
#2. Type this in Terminal: open tj.html
#  ~ this opens the file in your browser

toDo = [
        "Go to Barnes & Nobel",
        "Make crepes together",
        "Visit Fiji",
        "Bang",
        "Massage each other"
       ]

print("<html>")

print()

print("\t<head>")
print("\t\t<title>HappyDays</title> ")
print("\t</head>")

print()

print("\t<body>")
print("\t\t<h1>Making the Maxx of T&J's Future</h1>")

print()

print("\t\t<ul id=\"ourList\">")
for x in toDo:
    print("\t\t\t<li>" + x + "</li>")
print("\t\t</ul>")

print()

print("\t</body>")

print()
print("</html>")

