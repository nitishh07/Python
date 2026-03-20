# Escape seq characters

a = "Harry is a good boy\nbut a bad boy" # \n is used to break the line and print the next part in a new line
print(a)


b = "Harry is a good boy\nbut a bad \'boy\'" # \' is used to print a single quote in the string
print(b)

# Q1: Take input from the user and print a greeting message using that input.

name = input("Enter your name: ")

print("Good Afternoon" + name)
print(f"Good Morning {name}" ) # f is used to format the string and print the value of name in the string

# Q2 : Take input from the user and print a letter using that input.

date = input("Enter the date: ")
letter = '''Dear <|Name|>,
You are selected for the interview on <|date|>.'''

print(letter.replace("<|Name|>", name).replace("<|date|>", date))


# Q3 : Find the index of the first occurrence of a substring in a string
name = "Harry is a good  boy"
print(name.find(" ")) # find is used to find the index of the first occurrence of the substring "good" in the string name

# Q4 : Replace all occurrences of a substring in a string
print(name.replace("  ", " ")) # replace is used to replace all the occurrences of the substring " " with "_" in the string name