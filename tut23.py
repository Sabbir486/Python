# List Methods---->

l = [11,9,23,2,4,5,2,6,2,2]
print(l)

# Append Method--> Add new element
l.append(7)
print(l)
print()

# Sort Method---> Sorting Elements
l.sort()
print(l)
l.sort(reverse=True) #desending order
print(l)
print()

# Reverse Method
l.reverse()
print(l)
print()

# Index Method
print(l.index(23))
print()

# Count Method
print(l.count(2))
print()

# Copy Method
m = l.copy()
m[2] = 5
print(m)
print()

# insert Method
l.insert(1,200)
print(l)
print()

# extend Method
n = [200,300,400,500]
l.extend(n)
print(l)
print()

# Concating two lists
k = l+m
print(k)
