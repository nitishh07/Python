# q1

def greatest(a , b , c):
    if(a > b and a > c):
        print("a is greatest")
    elif(b > a and b > c):
        print("b is greatest")
    else:
        print("c is greatest")
        
greatest(1,2,3)


# Avoid new line
# print("a")
# print("b")
# print("c", end= "")
# print("d", end="")

# Sum

def sum(n):
    if(n == 1):
        return 1
    return sum(n-1) + n

print(sum(4))


def pattern(n):
    if(n == 0):
        return
    print("*" * n)
    pattern(n-1)
    
pattern(3)


# python func to remove a word from a list and strip it at the same time

# l = ["Harry" , "Rohan" , "Shubham" , "an"]

# def rem(l , word):
#     n = []
#     for item in l:
#         if not(item == word):
#             n.append(item.strip(word))
#     return n
    
# print(rem(l , "an"))


def rem(l, word):
    n = []
    for item in l:
        if item != word:
            n.append(item.replace(word, ""))
    return n

print(rem(l, "an"))