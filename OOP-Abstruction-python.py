from abc import ABC, abstractmethod


# Never Object will be created for abstract class
class Phone(ABC):
    def __init__(self, name, model):
        self.name = name
        self.model = model

    @abstractmethod
    def view(self):  # Abstraction
        pass


# --------------------sub class
class Oppo(Phone):
    def __init__(self, name, model, price):
        super().__init__(name, model)
        self.price = price

    def view(self):
        print("Name: ", self.name, " Model: ", self.model, " Price: ", self.price)


# --------------------sub class
class Samsung(Phone):
    def __init__(self, name, model, price):
        super().__init__(name, model)
        self.price = price

    def view(self):
        print("Name: ", self.name, " Model: ", self.model, " Price: ", self.price)


oppo = Oppo("Oppo", "F1", 12000)
oppo.view()

samsung = Samsung("Samsung", "A21s", 16990)
samsung.view()
