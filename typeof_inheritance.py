# # Simple Inheritance Example 
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
      

# # Multilevel  Inheritance Example 
# class Animal:
#    def __init__(self,name):
#       self.name=name
#    def speak(self):
#       print(f"{self.name} Barks/meow.")

# # Derived class
# class Dog(Animal):
#    def __init__(self,name):
#       super().__init__(name)
    
   
#    def speak(self):
#       print(f"{self.name} barks lauder than other animals.")

# class Puppy(Dog):
#    def __init__(self,name):
#       super().__init__(name)
    
   
#    def speak(self):
#       print(f"{self.name} barks cutely.")      

# obj1=Puppy("tommy")
# obj1.speak()


# # Hierarchical  Inheritance Example 
# # Base class
# class Animal:
#    def __init__(self,name):
#       self.name=name
#    def speak(self):
#       print(f"{self.name} Barks/meow.")

# # Derived class
# class Dog(Animal):
#    def __init__(self,name):
#      super().__init__(name)
   
#    def speak(self):
#       print(f"{self.name} barks lauder than other animals.")

# class Cat(Animal):
#    def __init__(self,name):
#      super().__init__(name)
   
#    def speak(self):
#       print(f"{self.name} meow lessor than other animals.")      

# obj1=Dog("tommy")
# obj1.speak()
# obj2 = Cat("whiskers")
# obj2.speak()
      

# # Multiple  Inheritance Example 
# # First parent class
# class Animal:
#    def __init__(self,name):
#       self.name=name
#    def speak(self):
#       print(f"{self.name} Barks.")

# # Second parent class
# class Dog:
#    def __init__(self):
#      self.nature='Friendly'
   
#    def behaviour(self):
#       print(f"{self.name} nature is {self.nature}.")

# # child class inheriting from both Animal and Dog
# class Puppy(Animal,Dog):
#    def __init__(self,name):
#      Animal.__init__(self,name)
#      Dog.__init__(self)   
#    def speak(self):
#       print(f"{self.name}'s barks louder than other animals.")      

# obj1=Puppy('Tommy')
# obj1.speak()
# obj1.behaviour()
      


# Hybrid  Inheritance Example 
# First parent class
class Animal:
   def __init__(self,name):
      self.name=name
   def speak(self):
      print(f"{self.name} Barks.")

# Second parent class
class Dog:
   def __init__(self):
     self.nature='Friendly'
   
   def behaviour(self):
      print(f"{self.name} nature is {self.nature}.")

# child class inheriting from both Animal and Dog
class Puppy(Animal,Dog):
   def __init__(self,name):
     Animal.__init__(self,name)
     Dog.__init__(self)   
   def speak(self):
      Animal.speak(self)
      print(f"{self.name}'s barks louder than other animals.")      

obj1=Puppy('Tommy')
obj1.speak()
obj1.behaviour()

      
      


      


      

      
      


      


      
      


      


      

      
      


      
