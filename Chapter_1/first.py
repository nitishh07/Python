print("Hello World")

import pyjokes

joke = pyjokes.get_joke()
print(joke)

'''This is a multi-line comment'''

# write a proram to print contents of directory in os module
import os
print(os.listdir())

# select the directory whose content  u want to use
directory_path = r"C:\Users\KIIT0001\Desktop\Python\Chapter_1"

#use os module to list the directory content
contents = os.listdir(directory_path)
print(contents)