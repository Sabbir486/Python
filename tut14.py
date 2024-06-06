# if-else statement

a = int(input("Enter Your Age: "))
print("Your age is: ", a)

if(a>18):
    print("You can drive")
else :
    print("You cannot drive")

print()

# Conditional Operators---> >, <, >=, <=, ==, !=
    
# print(a>18)
# print(a<18)
# print(a>=18)
# print(a<=18)
# print(a==18)
# print(a!=18)
    
# elif statement
a1 = int(input("Enter Your Age: "))
print("Your age is: ", a1)

if(a1>18):
    print("You can drive")
elif(a1==18):
    print("You can drive but be careful")
else :
    print("You cannot drive")

print("I am Sabbir\n")

# Nested if statement

num = 18

if(num<0):
    print("Number is negative")
elif(num>0):
    if(num<=10):
        print("Number is between 1-10")
    elif(num>10 and num<20):
        print("Number is between 11-18")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")

