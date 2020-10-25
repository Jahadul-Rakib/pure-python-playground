# Numeric Data Type ****************************************************************************************************

# Integer
x = 10
print(type(x))

# Float
y = 10.10
print(type(y))

# Complex
z = 10 + 1j
print(type(z))

# Boolean
print(type(x < y))

# Sequence Data Type ***************************************************************************************************

# String ---------------------------------------------------------------------------------------------------------------
x = " Rakib Demo"
print(type(x))  # Get Value Type
print(x[0])  # Get Value By Index Number
print(x[2:5])  # Get Value By Index Number between Index
print(x[-4:-2])  # Get Reverse Order By Index Number
print(len(x))  # Get String Lengh
print(x.strip())  # Remove White Space
print(x.upper())  # Convert Upper Case
print(x.lower())  # Convert Lower Case
print(x.replace(" ", "Jahadul"))  # Replace String
print(x.split())  # Split String

# List -----------------------------------------------------------------------------------------------------------------
# -------------Ordered and Changeable

mylist = [1, ["Sunno", "rakib", "dilruba"], 3, 3, 4, 5]
print(type(mylist))
print(mylist[1])
print(mylist[1][2])  # get Nested List Value

mylist = mylist + ["week", "sandar"]  # add list with list
print(mylist)
# or
mylist.extend([8, 20, 54])
print(mylist)

mylist.remove(mylist[1])  # remove from list
print(mylist)

print(mylist.count(3))  # count a value how much time comes

# Set ------------------------------------------------------------------------------------------------------------------
# -------------Ordered, Changeable and Contain Unique value
x = {1, 2, 3, 4, 5}
print(type(x))
y = set([8, 6, 23])  # convert list to set using set method
print(y)
y.add(24)  # add element
print(y)
# or
y.update([3, 4, 5])
print(y)
# or
s1 = {33, 44, 55}
y.update(s1)
print(y)

y.remove(55)  # remove element
print(y)
# or
y.discard(44)

s2 = x.intersection(y)  # get set intersection( common between them)
print(" Intersection ")
print(s2)

s3 = x.difference(y)  # get set difference( common between them)
print(" Difference ")
print(s3)

s1 = {33, 44, 55}  # Set Union Concept
s2 = {331, 443, 552}
s3 = {133, 144, 155}
print("Union")
s4 = s1.union(s2, s3)
print(s4)

# Tuple ----------------------------------------------------------------------------------------------------------------
# -------------Ordered and unChangeable
x = (1, 2, 3, 4, 5)
print(type(x))
del x  # only tuple can be deleted but its memory efficient

# Range ----------------------------------------------------------------------------------------------------------------
x = range(1, 7)
print(x)
print(type(x))

# Dictionary Data Type *************************************************************************************************

d1 = {"name": "Rakib", "Age": "23"}
d2 = {"name": "Sunno", "Age": "23"}
d3 = {"name": "Jahadul", "Age": "23"}
# copy one dictionary to other
d4 = d3.copy();

# add property in dictionary
d3["Home"] = "Valuka"
print(d3)

# delete property
d3.pop("Home")
print(d3)

# make empty
d3.clear()
print(d3)

d5 = {1: "Jahadul", 2: "23"}
print(d5.get(1))  # get by key
print(d5.items())  # get all item
print(d5.keys())  # get all Keys

# nested Dictionary
nd1 = {1: {1: "Jahadul1", 2: "23"},
       2: {1: "Jahadul2", 2: "23"},
       3: {1: "Jahadul3", 2: "23"},
       4: {1: "Jahadul4", 2: "23"}}
print(nd1)
print(nd1[1][2]) #data access
# add date
nd1[5] ={5: "Jahadul5", 2: "23"} # add
print(nd1)

del nd1[2] #delete
print(nd1)