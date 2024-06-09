# List--->
# List is changeable but tupple is not changeable
# index-->(0 to (n-1))
# length--> n

marks = [3,5,6, "Sabbir", True,8,10,4,4,5]
print(marks)
print(type(marks))

print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print()

print(marks[-3]) 
#Negative indexing---->(5-3)=2nd index
# Covert negative index into positive and then calculate it

# Searching elements in List

if 7 in marks:
    print("Yes")
else:
    print("No")

# Same things applies for strings as well
if "bbir" in "abbir":
    print("Yes")
else:
    print("No")

print(marks[:])
print(marks[2:])

# Jump Index

print(marks[1::2])
print()

# List Comprehension---> Create a new list on the fly

lst1 = [i for i in range(10)]
print(lst1)

lst = [i*i for i in range(10) if i%2==0]
print(lst)