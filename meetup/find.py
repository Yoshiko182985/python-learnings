#Array - a list
#in this program, we'll print the smallest number in the array

#Turn this into a function!
# getMin takes an array and returns the smallest

def getMin (nums):
    min = nums[0]

    for x in nums:
        if x <= min:
            min = x
    return min

def getMax (nums):
    max = nums[0]

    for x in nums:
        if x >= max:
            max = x
    return max

nums = [-2, 45, 62, 18, 45, 92, 5, 23, 79, -1, -5]

smallest = getMin(nums)
largest = getMax(nums)
print("The smallest number in your list is", smallest)
print("The biggest number in your list is", largest)
