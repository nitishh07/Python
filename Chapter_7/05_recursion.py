'''
factorial(1) = 1
factorial(n) = n x n-1 x ........3x2x1
factorial(n) = n * factorial(n-1)
'''

def factorial(n):
    if(n == 1 or n == 0):
        return 1
    return n * factorial(n-1)

n = int(input("Enter a number : "))
print(f"The factorial of this number is : {factorial(n)}")