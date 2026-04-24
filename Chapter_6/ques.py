# Print table

# n = int(input("Enter a number: "))

# for i in range(1, 11):
#     print(f"{n} X {i} = {n * i}")
    
    

# n = int(input("Enter a number: "))

# i = 1

# while(i < 11):
#     print(f"{n} X {i} = {n * i}")
#     i +=1 
    

# l = ["Harry", "Soham", "Sachin", "Suresh"]

# for name in l :
#     if(name.startswith("S")):
#         print(f"Hello {name}")
    


# wheter a no is prime or not

# x = int(input("Enter a number : "))

# for i in range(2 , n):
#     if(x%i == 0):
#         print("No. is not prime")
#         break
#     else:
#         print("No is prime")
        

# sum

# i = 1
# sum = 0
# while(i<x):
#     sum += i
#     i+=1

# print(sum)


# factorial

# product = 1
# for i in range(1 , x+1):
#     product = product * i

# print(f"The factorial is : {product}")



'''
    *
   ***
  *****
'''

n = int(input("Enter a no. : "))
for i in range(1 , n+1):
    print(" "*(n-i), end = "")
    print("*"* (2*i-1), end= "")
    print("")


for i in range(1 , n+1):
    if(i == 1 or i==n):
        print("*"* n , end = "")
    else:
        print("*", end = "")
        print(" "* (n-2), end= "")
        print("*", end="")
    print("")



for i in range(1,11):
    print(f"{n} X {11 - i} = {n*(11-i)}")