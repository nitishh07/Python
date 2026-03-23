# # Q1
# words = {
#     "aam" : "mango",
#     "rani" : "queen",
# }

# # word = input("Enter the word you want meaning of : ")
# # print(words[word])

# # Q2

# a = input("Enter the no. : ")
# # s.add(int(n))
# b = input("Enter the no. : ")
# # s.add(int(n))
# c = input("Enter the no. : ")
# d = input("Enter the no. : ")
# e = input("Enter the no. : ")
# f = input("Enter the no. : ")

# set = {a,b,c,d,e,f}

# print(set)


# Q 3
s = set()
s.add(20)
s.add(20.0)
s.add('20')
print(len(s))  #  2 bcz in python 20 == 20.0 is True

# Q4 -  create a dict with name & lang then update the value an check the same is valid or the same value is valid

d = {}
name = input("Enter friends name :")
lang = input("Enter language name : ")
d.update({name : lang})

name = input("Enter friends name :")
lang = input("Enter language name : ")
d.update({name : lang})

name = input("Enter friends name :")
lang = input("Enter language name : ")
d.update({name : lang})

name = input("Enter friends name :")
lang = input("Enter language name : ")
d.update({name : lang})

print(d)

# if key is same to update ho jaega - val
# val same ho skta hai dict me


# Q5 - can u change the values inside a list which is contained in Set S
'''Set me sirf immutable (fixed) values allowed hoti hain
List mutable hoti hai (change ho sakti hai)
Isliye Python list ko set ke andar allow hi nahi karta'''

s = {8 , 7 , 12 , "Harry" , [1,2]}

s[4][0] = 9

print(s)

