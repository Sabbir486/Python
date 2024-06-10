# f-strings in python---> Use for formating string

letter = "Hey my name is {} and I am from {}"
country = "Bangladesh"
name = "Sabbir"

# print(letter.format(country,name))
print(f"Hey my name is {name} and I am from {country}")

price = 50.09456732
txt = f"For only {price:.2f} dollars!"
print(txt)

