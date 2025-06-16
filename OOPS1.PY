class employee:
   # special method / magic method /dunder method constructor 
   def __init__(self):
      print("started executing attributes of the employee class ")
      self.id=123
      self.salary=50000
      self.designation="Software Engineer"
      print("end of the attributed class in the employee class")


# this is the called the method  because it is used in  the class that is the reason it is called method 
   def travel(self,destination):
      print("I am travelling to manually")
      print(f"I am travelling to {destination}")
# creating an object of employee class 
ali=employee()

# print(ali.id)
# print(ali.salary)
# print(ali.designation)
# ali.travel("Delhi")
print(type(ali))