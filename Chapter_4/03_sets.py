# s = {1 , 5 , 32}

#empty set
e = set()  # don't use s = {} as it will create an empty dictionary

# Elemnts can'tbe repeated in sets
s = {1,5,32,54,5,5 , "Harry"}

s.remove(1)
# s.clear() - empty the set
# s.pop() - rmeoves random elemnt from set
print(s)


# Uninon and intersection
s1 = {1,4, 5,6}
s2 = {1,5,23,90}

print(s1.union(s2))
print(s1.intersection(s2))

# isusbset()