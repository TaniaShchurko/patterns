from abc import abstractmethod

class Product:
    @abstractmethod
    def cook(self): pass

class Carbonara(Product):

    def __init__(self, name = "Carbonara"):
        self.__name = name

    def cook(self):
        print(f"Italian main dish: {self.__name}")

class Panettone(Product):

    def __init__(self, name = "Panettone"):
        self.__name = name

    def cook(self):
        print(f"Italian dessert: {self.__name}")

class Ratatouille(Product):

    def __init__(self, name = "Ratatouille"):
        self.__name = name

    def cook(self):
        print(f"French dish: {self.__name}")

class CremeBrulee(Product):

    def __init__(self, name = "CremeBrulee"):
        self.__name = name

    def cook(self):
        print(f"French dessert prepared: {self.__name}")

class Factory:
    @abstractmethod
    def get_dish(self, type_of_meal): pass

class ItalianDishesFactory(Factory):
    def get_dish(self, type_of_meal):
        return Carbonara() if type_of_meal == "main" else Panettone()

class FrenchDishesFactory(Factory):
    def get_dish(self, type_of_meal):
        return Ratatouille() if type_of_meal == "main" else CremeBrulee()

class FactoryProducer:
    def get_factory(self, type_of_factory):
        return ItalianDishesFactory() if type_of_factory == "italian" else FrenchDishesFactory()


fp = FactoryProducer()
fac1 = fp.get_factory("italian")
fac2 = fp.get_factory("french")
main_dish1 = fac1.get_dish("main")
dessert1=fac1.get_dish("dessert")
main_dish2 = fac2.get_dish("main")
dessert2=fac2.get_dish("dessert")
main_dish1.cook()
dessert1.cook()
main_dish2.cook()
dessert2.cook()