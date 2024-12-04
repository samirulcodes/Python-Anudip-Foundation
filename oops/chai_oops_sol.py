# Basic Class and Object
# Problem: Create a Car class with attributes like brand and model. Then create an instance of this class.
# Add a method to the Car class that displays the full name of the car (brand and model).

'''
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        
    # defining another methods(functionality)
    def fullName(self):
        return f"{self.brand} {self.model}"
    
# creating object 1
obj1=Car("Mahindra","Thar")
print(obj1.brand)
print(obj1.model)
print(obj1.fullName())

# creating object 2
obj2=Car("Tata","Safari")
print(obj2.brand)
''' 


# Inheritance
# Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.
'''
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        
    # defining another methods(functionality)
    def fullName(self):
        return f"{self.brand} {self.model}"
    
class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand,model)  # super -- keyword take access of parent class 
        self.battery_size=battery_size
        
# creating object for ElectricCar class

obj = ElectricCar("Tesla", "Model S", "85kWh")
print(obj.model)
print(obj.brand)
print(obj.battery_size)
print(f"Printing together: {obj.fullName()}")

''' 
# creating object for Car class
# obj1 = Car("Mahindra","Thar")
# print(obj1.brand)
# print(obj1.model)
# print(obj1.fullName())


# Encapsulation
# private declaration= __variableName , eg--> __model(it become private)
class Car:
    def __init__(self,brand,model):
        self.__brand=brand
        self.model=model
        
    # defining another methods(functionality)
    def fullName(self):
        return f"{self.__brand} {self.model}"
    
    # getter method
    def get_brand(self):
        return self.__brand + " is a good brand "
    
class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand,model)  # super -- keyword take access of parent class 
        self.battery_size=battery_size
        
# creating object for ElectricCar class

obj = ElectricCar("Tesla", "Model S", "85kWh")
# print(obj.__model) # this model is now private it can't access by object and accessible within class
print(obj.get_brand())  # this will be accessible as getter methods called
