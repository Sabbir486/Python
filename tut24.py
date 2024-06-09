# Tupples--->
# Tupples are unchangeable

tup = (1, "green", 5,7,8,9)
print(type(tup))
print(len(tup))
print(tup)
print(tup[0])
print(tup[1])
print(tup[-2])
print()

if "green" in tup:
    print("Yes")
    
tup2 = tup[1:3]
print(tup2)