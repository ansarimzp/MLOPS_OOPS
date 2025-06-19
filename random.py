# Mlops series from starting to end means beginners to advance level 

# MLOPS OOPS Concept in simple words with example 

class chatbook:   #  class of the  mlops series 

# this is show the attributes/data or this is also called the constructor of the class 
     def __init_(self): 
            self.username=''
            self.password=''
            self.menu()
            self.designation=False
# method/function of the class in mlops series 

     def menu(self):
        while(True):
             print("\n Please choose an options--> ")
             print("1. Sign Up")       
             print("2. Sign In")
             print("3. Write a Post")
             print("4. Message a Friend")
             print("5. Set Display Name")
             print("6. Exit")
             
             choice= input("Enter your choice(1-6): ")
             if choice=='1':
                  self.signup()
             elif choice=='2':
                  self.signin()
             elif choice=='3':
                  self.write_post()
             elif choice=='4':
                  self.send_message()
             elif choice=='5':
                  self.st_name()
             elif choice=='6':
                 print(" Thanks for using Chatbook! Goodbye. ")
                 break
             else:
                 print("Invaid choice. Please enter a number between 1-6")
   
   

     def signup(self):
       print("Sign Up: ")
       self.username= input("Enter your email/username: ")
       self.password= input("Enter your password: ")
       print("You have successfully signed up!")
       print("\n")
       self.menu()


   
     def signin(self):
       if self.username=='' and self.password=='':
           print(" Please sign up first before trying to log in.")
           return 
       uname= input("Enter your email/username: ")
       pwd= input("Enter your password: ")

       if uname== self.username and pwd==self.password:
          print("Login successfully!") 
          self.loggedin=True
       else:
           print("Incorrect username or password!")
       print("\n")
       self.menu()
   


  
     def write_post(self):
       if self.loggedin==True:
          text= input("Write your post here-->   ")
          print("You have write your post successfully ")
       else:
           print("You have sign in firstly in this Chatbook")
       print("\n")
       self.menu()
   
     def send_message(self):
       print("send message: ")
       if  self.loggedin:
           friend=input("Enter your friend name: ")
           message= input("Enter your message: ")
           print(f"Message send to {friend}: \"{message}\"")
       else:
           print("Please sign in to send the message.")
     def set_name(self):
       name= input("Enter your display name: ")
       self.name=name
       print(f"Display name set to {self.name}.")

     def get_name(self):
      return self.name
    

object1= chatbook()
object1.menu()

       
       


         
