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
'''
class Car:
    def __init__(self,brand,model):
        self.__brand=brand
        self.model=model
    
    # getter method
    def get_brand(self):
        return self.__brand + " is a good brand "
    
     # defining another methods(functionality)
    def fullName(self):
        return f"{self.__brand} {self.model}"
    
class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand,model)  # super -- keyword take access of parent class 
        self.battery_size=battery_size
        
# creating object for ElectricCar class

obj = ElectricCar("Tesla", "Model S", "85kWh")
# print(obj.__model) # this model is now private it can't access by object and accessible within class
print(obj.get_brand())  # this will be accessible as getter methods called
''' 

# polymorphism
# Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.
'''
class Car:
    def __init__(self,brand,model):
        self.__brand=brand
        self.model=model
        
     # getter method
    def get_brand(self):
        return self.__brand + " is a good brand "
    
    # defining another methods(functionality)
    def fullName(self):
        return f"{self.__brand} {self.model}"
   
    # same name
    def fuel_type(self):
        return "Petrol or Diesel"
    
class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand,model)  # super -- keyword take access of parent class 
        self.battery_size=battery_size
    # same name
    def fuel_type(self):
        return "Electric Charge"
    
# creating object

obj = ElectricCar("Tesla", "Model S", "85kWh")
# print(obj.get_brand())  # this will be accessible as getter methods called
print(obj.fuel_type()) 

obj1=Car("Tata","Safari")
print(obj1.fuel_type())
''' 

# Class Variables
# Problem: Add a class variable to Car that keeps track of the number of cars created.
'''
class Car:
    total_car=0  #variable
     
    def __init__(self,brand,model):
        self.__brand=brand
        self.model=model
        # self.total_car +=1
        Car.total_car +=1  # tracking total num of car
        
    # getter method
    def get_brand(self):
        return self.__brand + " is a good brand "
    
    # defining another methods(functionality)
    def fullName(self):
        return f"{self.__brand} {self.model}"
   
    # same name
    def fuel_type(self):
        return "Petrol or Diesel"
    
class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand,model)  # super -- keyword take access of parent class 
        self.battery_size=battery_size
    # same name
    def fuel_type(self):
        return "Electric Charge"
    
# creating object
# car 1
obj = ElectricCar("Tesla", "Model S", "85kWh")
# print(obj.get_brand())  # this will be accessible as getter methods called
print(obj.fuel_type()) 

obj1=Car("Tata","Safari")  # car 2
print(obj1.fuel_type())

# printing for tracking toal no. of car
print(Car.total_car)  # o/p -- total car = 2
''' 


# static method
# Problem: Add a static method to the Car class that returns a general description of a car.
'''class Car:
    def __init__(self,brand,model):
        self.__brand=brand
        self.model=model
    
    # getter method
    def get_brand(self):
        return self.__brand + " is a good brand "
    
     # defining another methods(functionality)
    def fullName(self):
        return f"{self.__brand} {self.model}"
    
    @staticmethod  # decorators
    def geneal_description():  # as static method declare so need to connect with self or pass any self as an argument
        return "Cars are means of transport"
    
class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand,model)  # super -- keyword take access of parent class 
        self.battery_size=battery_size
        
# creating object for ElectricCar class

obj=Car("Tata","Safari")
print(obj.geneal_description())
print(Car.geneal_description())'''


# Property Decorators
# Problem: Use a property decorator in the Car class to make the model attribute read-only.

'''class Car:
    def __init__(self,brand,model):
        self.__brand=brand
        self.__model=model
    
    # getter method
    def get_brand(self):
        return self.__brand + " is a good brand "
    
     # defining another methods(functionality)
    def fullName(self):
        return f"{self.__brand} {self.__model}"
    
    @staticmethod  # decorators
    def geneal_description():  # as static method declare so need to connect with self or pass any self as an argument
        return "Cars are means of transport"
    
    # making read only to model(means once model declare it can't be change)
    @property
    def model(self):
        return self.__model
    
class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand,model)  # super -- keyword take access of parent class 
        self.battery_size=battery_size
        
# creating object for ElectricCar class

obj=Car("Tata","Safari")
# obj.model="City"
print(obj.model)'''


#  Multiple Inheritance
# Problem: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.

class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
    @property
    def model(self):
        return self.__model

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type():
        return "Electric charge"

class Battery:
    def battery_info(self):
        return "This is battery"

class Engine:
    def engine_info(self):
        return "This is engine"

class ElectricCarTwo(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCarTwo("Tesla", "Model S")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())
