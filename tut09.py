# Type Casting

# a = 1
# b = 2

a = "1"
b = "2"

print(int(a) + int(b))

# Type Casting---> Explicit, Implicit
# Explicit-->Done by ourselves
string = "15"
number = 7
string_number = int(string) #Throw an error if the string is not a valid integer
sum = number + string_number
print('The sum of both the numbers is: ', sum)

# Implicit--> Python converts a smaller data type to a higher data type to prevent data loss
c = 1.9
d = 8
print(c+d)
print(type(c+d))