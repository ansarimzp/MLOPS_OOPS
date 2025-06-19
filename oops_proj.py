class chatbook:

   __user_id=1
   def __init__(self):
      self.id= chatbook.__user_id
      chatbook.__user_id+=1
      # print(f"Welcome to chatbook !! Your user id is {self.__user_id}")
      self.__name='Default user'
      self.username =''
      self.password=''
      self.loggedin=False
      # self.menu()
   
   @staticmethod 
   def get_id():
      return chatbook.__user_id
   @staticmethod
   def set_id(val):
      chatbook.__user_id=val


   def get_name(self):
      return self.__name
   def set_name(self,name):
      self.__name=name
      print(f"Your name set to {self.name} !!")
   def get_name(self):
      return self.__name   

   def menu(self):
      user_input= input("""Welcome to chatbook !! how would you like to proceed?
                        
                        1. Pess 1 to signup
                        2. Press 2 to signin
                        3. Press 3 to write a post
                        4. Press 4 to message a friend
                        5. Prss any other key to exit  """ )

      if user_input=='1':
         self.signup()
      elif user_input=='2':
         self.signin()
      elif user_input=='3':
         self.write_post()
      elif user_input=='4':
         self.sendmessage()
      else:
         print("Thanks for using chatbook !!")

   def signup(self):
       email=input("Enter your email here--> ")
       password=input("Enter your password here --> ")
    
       self.username=email
       self.password=password
       print("You have successfully singed up in chatbook !!")
       print("\n")
       self.menu()



   def signin(self):
      if(self.username=='' and self.password==''):
         print("You need to signup first !!")
      else:
         uname=input("Enter your email/username here -->")
         pwd=input("Enter your password here -->")
         if self.username==uname and self.password ==pwd:
            print("You have successfully signed in !!")
            self.loggedin=True
         else:
            print("Plese check your username or password !!")
      print("\n")
      self.menu()


   def write_post(self):
      if self.loggedin==True:
         txt= input("Write your post here -->")
         print("Your post has been successfully posted !!")
      else:
         print("You need to sign in first !!")    

      print("\n")
      self.menu()

   def sendmessage(self):
      if self.loggedin==True:
         txt= input("Write your message here -->")
         friend=input("Whom to send the message? -->")
         print(f"Your message has been successfully sent to your {friend} !!") 

      else:
         print("You need to sign in first !!")
      print("\n")
      self.menu()        


# obj=chatbook()
# obj.name()
# obj.set_name("Seraj")     
   