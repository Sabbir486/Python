# String

name = "Sabbir"
friend = 'Roni'

print (name + friend + " are friend")

# It's not possible, double quatation under double quatation....So, we use double quatation uder single quatation in a string.
apple = 'He said, "I want to eat an apple'
print(apple)
print()

# Under triple quatation, anything become String.

apple1 = '''He said,
I am Roni
I am Good 
"I want to eat an apple'''

print(apple1)
print()

print(name[0])
print(name[4])
print()
# print(name[6]) #Throws an error

for character in apple1:
    print(character)