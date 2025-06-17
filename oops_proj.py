class chatbook:
   def __init__(self):
      self.username =''
      self.password=''
      self.loggedin=False
      self.menu()

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
         pass
      elif user_input=='4':
         pass
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

obj=chatbook()
     
   