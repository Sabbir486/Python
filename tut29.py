# Docstrings in Python---> To understand a function properly
# Like comments but not comments.

def square(n):
    # docstring must put right below the function name
    ''' Takes in a number n, returns the square of n'''
    print(n**2)
square(5)
print(square.__doc__)

# import this ---> PEP8 opened in terminal