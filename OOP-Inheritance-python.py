# Inheritance Concept
# --------------------super class
class Phone:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def view(self):  # Abstraction
        pass


# --------------------sub class
class Oppo(Phone):
    def __init__(self, name, model, price):
        super().__init__(name, model)  # Pass value to super class constructor
        self.price = price

    def view(self):  # Method Overriding
        print("Name: ", self.name, " Model: ", self.model, " Price: ", self.price)


# --------------------sub class
class Samsung(Phone):
    def __init__(self, name, model, price):
        super().__init__(name, model)  # Pass value to super class constructor
        self.price = price

    def view(self):  # Method Overriding
        print("Name: ", self.name, " Model: ", self.model, " Price: ", self.price)


oppo = Oppo("Oppo", "F1", 12000)
oppo.view()

samsung = Samsung("Samsung", "A21s", 16990)
samsung.view()
