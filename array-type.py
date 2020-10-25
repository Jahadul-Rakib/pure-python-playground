from array import *

salary = array("i", [2300, 3400, 1200, 30000])
print(salary[0])

for i in range(4):
    print(salary[i])

salary.append(2222)  # add value in array
print(salary)

salary.remove(2300)  # remove value from array
print(salary)

salary.reverse()  # get reverse order
print(salary)
