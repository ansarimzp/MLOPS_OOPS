class Animal:
   def __init__(self, name):
      self.name = name
      self.age = 2
      self.sound_type = 'meow'
   def sound(self):
      print(f"{self.name} makes sound {self.sound_type}")   

class Cat(Animal):
   pass  

class dog(Animal):
   pass
   
# Uncomment the following method to override the sound method in the Cat class
#   def sound(self):
#      print("cat is making sound like meow") 

object1 = Cat("sona")
object1.sound()      