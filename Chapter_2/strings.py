# Strings is immutable
name = "Harry"

# Indexing
nameshort = name[0:3] # start from index 0 all the way to index 3 (excluding 3)
print(nameshort)

# print character 
char1 = name[1]
print(char1)


# negative slicing
# Nitish (0 ,1 ,2,3,4,5) (-6, -5, -4, -3, -2, -1) indexing from left to right and right to left
print(name[-4:-1])

print(name[:6])  # :4 means start from index 0 and go all the way to index 4 (excluding 4)
print(name[2:])  # 2: means start from index 2 and go all the way to the end of the string

# Skip Value

char = "123456789"
print(char[0:5:2])  # start from index 0 to index 5 (excluding 5) and skip every 2 characters
print(char[1:4])

# length of name
print(len(name))
print(char.endswith("ry"))  # check if the string ends with "ry"
print(char.startswith("ry"))
print(name.capitalize())