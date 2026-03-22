marks = {
    "Harry" : 100,
    "Shubham" : 45,
    "Rohan" : 67,
}

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Harry" : 99 , "Pihu" : 101}) 
print(marks)

print(len(marks))  #length

print(marks.get("Harry")) # Prints none if key not found
print(marks["Harry"]) # Prints error if key not found