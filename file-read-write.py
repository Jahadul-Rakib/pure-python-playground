# File IO


#Reading
file = open("files/student.txt", "r+")  # r for read, w for write, r+ read and write
print(file.readable())
#read all
text = file.read()
print(text)
# or Line By Line
text = file.readline()
print(text)
# or Line By Line All and can accessable by index
text = file.readlines()
print(text)
#Using Loop
for line in file:
    print(line)
file.close()


#Writing

file = open("files/student.txt", "a") # a means append mode
file.write("\n hello rakib.")

file = open("files/student1.txt", "a") # it will create automatically new file if not exis in write mode
file.write("\n hello rakib.")

file.close()