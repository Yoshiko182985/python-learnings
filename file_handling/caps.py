import sys

if len(sys.argv) == 3:

    ogfile = sys.argv[1]
    #newfile = "CAPS_" + ogfile.upper()
    newfile = sys.argv[2]

    og = open(ogfile, "r")
    n = open(newfile, "w")
    numLine = 0

    for line in og:
        n.write(line.upper())
        numLine = numLine + 1

    print("Successfully copied", numLine, "lines to", newfile, "!")

    og.close()
    n.close()

else:
    print("Usage:", sys.argv[0], '"originalfile" "newfile"')
