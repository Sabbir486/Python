# String Methods

a= 'Sabbir'
print(len(a))
print()

# Cocept of Immutability--->(Strings are immutable)
print(a.upper())
print(a.lower())
print()

a1= '!!Sabbir!!!!!!  Fahim  Sobuz Sabbir'
print(a1.rstrip("!"))

print(a.replace("Sabbir","Roni"))
print()

# Split Methods--->Become a list
print(a1.split())
print()

blogHeading = "introDuction to pYthon"
print(blogHeading.capitalize())
print()

print(len(blogHeading))
print(len(blogHeading.center(50)))
print (blogHeading.center(50))
print()

print(a1.count("Sabbir"))

# Endswith
print(blogHeading.endswith("n"))
print(blogHeading.endswith("n",2,8))
print()

print(blogHeading.find("pYthon"))
print(blogHeading.find("is"))
print()

# isalnum only considers (A-Z, a-z, 0-9)....Even space is also not considered here
print(blogHeading.isalnum())

blogHeading1 = "introDuctiontopYthon"
print(blogHeading1.isalnum())

# isalpha---> checks (A-Z, a-z)
# islower---> checks (lower case only)
# isprintable--> checks (all are printable or not)
# isspace---> checks (spaces)
#istitle---> checks ( is all the first later of words are in capital or not)
# startswith
# swapcase--->converts (lower to upper or upper to lower)
# title()
