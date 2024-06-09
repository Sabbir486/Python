# Function Arguments---->

# Default Arguments
def average(a,b):
    print("The average is: ", (a+b)/2)

average(4,6)

# Keyword Arguments

average(b=9, a=21)

# Required Arguments
# Variable-Length Arguments

def average1(*numbers):
    sum = 0
    for i in numbers:
        sum = sum+i
    print("Average1 is: ", sum/len(numbers))

average1(5,6,7,10,15)

print()

def average1(*numbers):
    sum = 0
    for i in numbers:
        sum = sum+i
    return sum/len(numbers)

c= average1(5,6,7,10,15)
print(c)
# Return fuction give the return value



