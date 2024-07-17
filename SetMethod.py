# writting a python program to create a set with different datatype

names = {"sankar", "lokesh", "rajesh", "sweetha"}

print(type(names))

# program to iterate ver set 
for item in names:
    print(item)

# program to add a member 
names.add("anil")
print(names)

# program to remove a member from set
names.remove("sweetha")
print(names)

# program to remove a member from set which is presence in set
names.discard("sankar")
print(names)

# program to create a interaction in set
names2 = {"anil", "radha", "krishna", "lokesh"}
print(names.intersection(names2))

# difference between two step

print(names)
print(names2)
names3 = names.symmetric_difference(names2)

print(names3)