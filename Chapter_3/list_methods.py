friends = ["Apple" , "Orange" , 5 , 345.06, False , "Harry"]

friends.append("Mango") # Adds "Mango" to the end of the list
print(friends)

l1 = [1,3,4,2,1]
l1.sort() # Sorts the list in ascending order
print(l1)

l1.reverse()
print(l1)

# insertion (idx , val)
l1.insert(3, 33333) # idx , object 
print(l1)

# pop
value = l1.pop(3)
print(value)
print(l1)

# remove - find and remove
l1.remove(2)
print(l1)