class Student:
    id = "",
    name = "",
    subject = ""

    def set_value(self, id, name, subject):  # value inject by a user define method
        self.id = id
        self.name = name
        self.subject = subject

    def display(self):
        print(f"Id: {self.id}, Name: {self.name}, Subject: {self.subject}")


rakib = Student();
rakib.id = 1
rakib.name = "Rakib"
rakib.subject = "IT"
rakib.display();

rohim = Student();
rohim.set_value(2, "Rohim", "CSE")
rohim.display();


# -----------------------------------------------------------------------------------------------------------------------

class Employee:
    def __init__(self, id, name):  # Constructor by __init__ method
        self.id = id
        self.name = name

    def display(self):
        print(f"Id: {self.id}, Name: {self.name}")


dilruba1 = Employee(1, "Dilruba")
dilruba1.display()
dilruba2 = Employee(2, "Dilruba2")
dilruba2.display()
