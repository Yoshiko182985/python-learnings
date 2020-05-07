# The goal of this program is to make a multiplication table
# N represents the size of the table, which is customizable

N = 20
# this runs in O(N^2)
for x in range(1, N+1):
    for y in range (1, N+1):
        print(y * x, end = "\t")
    print()

