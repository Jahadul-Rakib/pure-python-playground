import functools


# function

def add_number(x, y):
    return x + y


def sub_number(x, y):
    return x - y


print(add_number(12, 2))
print(sub_number(12, 2))


# any number of peramiter function

def take_number(*data):
    print(data)


take_number(1, 2, 3)
take_number(1, 2, 3, 4)
take_number(1, 2, 3, 4, 5)
take_number(1, 2, 3, 4, 5, 6)


# function take key value pair parameter

def function(**data):
    return print(data)


function(id=1, name="rakib")

# Lambda function
# Single line Expression
# Lambda Keyword then Keys then condition then Values
print((lambda a, b: a + b)(1, 2))


# Map and Filter

def square(x):
    return x * x


x = [1, 2, 3, 4, 5]

result = list(map(square, x))  # Map kept result which kept or not kept value
print(result)

result = filter(lambda x: x < 5, x)  # Filter remove those value which do not meet requirement
print(list(result))

# Reduce Method
# import functools
listOne = [1, 2, 34, 4, 5, 2]


def add_value(num1, num2):
    return num1 + num2


result = functools.reduce(add_value, listOne)
print("From Reduce ", result)
# List Comprehensive function
# [condition FOR receiver IN list]
result = [i * 2 for i in x]
print(result)

# Zip Function
x = [1, 2, 3, 4, 5, 6]
name = ["rakib", "monir", "Roni", "bili"]

result = list(zip(x, name, "ABCDEF"))
print(result)

# Lambda function
result = lambda x, y: x + y
print("From Lamda: ", result(2, 3))
# or
result = (lambda x, y: x + y)(2, 4)
print("From Lamda: ", result)

# Global variable

x = 100


def check():
    global x
    y = x + 10
    return print(y)
check()
print(x)