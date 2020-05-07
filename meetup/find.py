#This program runs some basic arithmatic, while practicing nested loops

import time

def getMin(nums):
    min = nums[0]

    for x in nums:
        if x <= min:
            min = x
    return min

def getMax(nums):
    max = nums[0]

    for x in nums:
        if x >= max:
            max = x
    return max

def avg(nums):
    a = 0

    for x in nums:
        a = x + a

    a = a / (len(nums))
    return a

def getMinMax(nums):
    min = nums[0]
    max = nums[0]
    for x in nums:
        if x >= max:
            max = x
        if x <= min:
            min = x
    return (min, max)


nums = [5, -15, 10]
t1 = time.time()

minmax = getMinMax(nums)
smallest = getMin(nums)
largest = getMax(nums)
average = avg(nums)

t2 = time.time()
delta = t2 - t1
print("Runtime took:", delta, "seconds")

print(minmax)
print("The smallest number in your list is", smallest)
print("The biggest number in your list is", largest)
print("The average of your list is", average)
