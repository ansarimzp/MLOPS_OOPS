
# Normal inheritance example in python 
# class Animal:
#    def __init__(self,name):
#       self.name = name
#    def speak(self):
#       print(f"{self.name} barks.")   
   

# object1 =Animal('Dog')
# object1.speak()


# child class accessing parent class method 
# Base class 
# class Animal:
#    def __init__(self,name):
#       self.name=name
#    def speak(self):
#       print(f"{self.name} Barks.")

# # Derived class
# class Dog(Animal):
#    # def __init__(self,name):
#    #    self.name=name
   
#    def speak1(self):
#       print(f"{self.name} barks lauder than other animals.")

# obj1=   Dog("tommy")
# obj1.speak()
      


# Base class encapsulation add in the constructor so child class can not access it directly 
# class Animal:
#    def __init__(self,name):
#       self.__name=name
#    def speak(self):
#       print(f"{self.name} Barks.")

# # Derived class
# class Dog(Animal):
#    def __init__(self,name):
#       self.name=name
   
#    def speak1(self):
#       print(f"{self.__name} barks lauder than other animals.")

# obj1=   Dog("tommy")
# obj1.speak()
      

# Private Base class 
# class _Animal:
#    def __init__(self,name):
#       self.name=name
#    def speak(self):
#       print(f"{self.name} Barks.")

# # Derived class
# class Dog(_Animal):
#    def __init__(self,name):
#       self.name=name
   
#    def speak1(self):
#       print(f"{self.name} barks lauder than other animals.")

# # obj1=Dog("tommy")
# # obj1.speak()
# obj2 = _Animal("tommy")
# obj2.speak()


# # Constructor overloading in inheritance 
# class Animal:
#    def __init__(self,name):
#       self.name=name
#    def speak(self):
#       print(f"{self.name} Barks.")

# # Derived class
# class Dog(Animal):
#    def __init__(self,name):
#       self.name=name
   
#    def speak(self):
#       print(f"{self.name} barks lauder than other animals.")

# obj1=Dog("tommy")
# obj1.speak()
# obj2 = Animal("tommy")
# obj2.speak()
      
      


# # Method overloading in inheritance 
# class Animal:
#    def __init__(self,name):
#       self.name=name
#    def speak(self):
#       print(f"{self.name} Barks.")

# # Derived class
# class Dog(Animal):
#    def speak(self):
#       print(f"{self.name} barks lauder than other animals.")

# obj1=Dog("tommy")
# obj1.speak()



# # Super function/method used in inheritance 
# # Base class
# class Animal:
#    def __init__(self,name):
#       self.name=name
#    def speak(self):
#       print(f"{self.name} Barks.")

# # Derived class
# class Dog(Animal):
#    def __init__(self,name):
#       super().__init__(name)
#       self.name=name
   
#    def speak(self):
#       super().speak()
#       print(f"{self.name} barks lauder than other animals.")

# obj1=Dog("tommy")
# obj1.speak()


# # Super keyword are used outside the child class in inheritance 
# #Base class


# class Animal:
#    def __init__(self,name):
#       self.name=name
#    def speak(self):
#       print(f"{self.name} Barks.")

# # Derived class
# class Dog(Animal):
#    def __init__(self,name):
#       super().__init__(name)
#       self.name=name
   
#    def speak(self):
#       print(f"{self.name} barks lauder than other animals.")

# obj1=Dog("tommy")
# obj1.super.speak()  # super are not accessed outside the child class


      


      
      


      
      
