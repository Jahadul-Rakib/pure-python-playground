# If Statement
a = 10
b = 12
c = 12
if a > b or a < b:
    print("Or True")

if a < b and c == b:
    print("And True")

# if and else if condition
if a == b:
    print(" A=B")
elif a < b:
    print(" a less then b")
else:
    print("Do not match any condition")

# Ternary Operation
number1 = 120
number2 = 100
print(number1 if number1 > number2 else number2)

# While Loop
i = 10
while i <= 20:
    if i == 19:
        print("Break")
        break
    elif i == 20:
        print("continue")
        continue

    print(i)
    i = i + 1

# for loop
a = 0
x = [1, 3, 34, 5, 2, 4, 7, 67, 54, 67]
for i in x:
    a = a + i
print(a)


