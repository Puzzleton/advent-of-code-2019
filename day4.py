input = '272091-815432'

output = 0

# Example steps to find the next valid password:
# Check 272091 as our start input (*** = INVALID)
# Find the next available password by copying the digit before the first descending value (277777)
# Find the next available password by increasing the number by 1 until it creates a descending value (277778, 277779, ***277780***)
# From the invalid descending value, the next valid password is created by copying the digit before the first descending value (277788)
# 277789
# ***277790*** copy -> 277799
# ***277800*** copy -> 277888

# def parseInputIntoNumbers():

# def passwordChecker(number):

# def findNextValidPassword(number): ??

# Parse the input
# Check the range start is valid password
# Find the next valid password (if possible)
# If another valid password is found, increase the output by 1 and check for another valid password
# If another valid password is not found, abort