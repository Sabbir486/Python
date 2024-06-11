# Recursion in Python---->

def factorial(n):
    if(n == 1 or n == 0):
        return 1
    else:
        return (n * factorial(n-1))

print(factorial(4))
print(factorial(5))

# Quick Quiz----> Program on Fibonacci Series

def fibonacci(f):
    if(f == 0 ):
        return 0
    elif(f == 1):
        return 1
    else:
        return (fibonacci(f-1) + fibonacci(f-2))
    
print(fibonacci(6))
