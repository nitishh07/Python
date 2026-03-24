# a = int(input("Enter your age : "))

# # if statemnt - 1
# if(a % 2 == 0):
#     print("Even")
# end of if statement 1
  
# if statemnt 2  
# if(a >= 18):
#     print("You are above the age of concent")
#     print("Good for you !")
# elif(a < 0):
#     print("You are entering an invalid age")
    
# elif(a == 0):
#     print("You are entering 0 which is an invalid age")
# else:
#     print("You are below the age of concent")
# # end of if statement 1

  
# p1 = "Make a lot of money"
# p2 = "buy now"
# p3 = "subscribe this"

# msg = input("Enter your comment : ")

# if((p1 in msg) or (p2 in msg) or (p3 in msg)):
#     print("This comment is a spam")
# else:
#     print("This comment is not a spam")
    

user = input("Enter your username : ")

if(len(user) > 10):
    print("It oontains more than 10 chars")
else:
    print("It contains less than 10 chars")