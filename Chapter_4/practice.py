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