def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Prompt the user for input
num1 = int(input("Enter a non-negative integer: "))

if num1 < 0:
    print("Factorial is not defined for negative numbers.")
elif num1 == 0:
    print("The factorial of 0 is 1.")
else:
    result = factorial(num1)
    print(f"The factorial of {num1} is {result}.")