#The goal of this program is to make a multiplication table

#for y in range(1, 11):
#    print (y * 1 , end = " ")
#print("\n")


#for y in range(1, 11):
#    print (y * 2 , end = " ")
#print("\n")


#for y in range(1, 11):
#    print (y * 3 , end = " ")
#print("\n")

##is this less than ten? if so, print a space!
#print("Let's test some $hit out!")
#print()

for x in range(1, 13):
    for y in range (1, 13):
        print(y * x, end = "\t")
    print()

