# Tupples Methods--->

# Manipulating Tupples:

countries = ("A","B", "C", "D")
temp = list(countries)
temp.append("Australia")
temp[2]= ("Argentina")
countries = tuple(temp)
print(countries)

# Cocatanation in Tupples

c1 = (2,3,5,6,1,7)
c2 = (11,13,14)
c = c1 + c2
print(c)

# Count Method 
# Index Method
d = (2,3,4,5,3,5,3,6,3,8)
res1 = d.index(3)
print(res1)
res2 = d.index(3,2,8)
print("Count of 3 in between 2nd index to 8th index: ",res2)
print()

# length Method
res3 = len(d)
print(res3)