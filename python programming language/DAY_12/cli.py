# choice - login, register
choice = input('''1. Register 
2. Login ''')
# if register,get username and password, store the username in a file

if choice == "1":
   username = input("Enter username:")
   password = input("Enter password")
   f = open('userdata.txt','a')
   f.write(f"{username}:{password},")
   print("Registation successfull")
   f.close()
# if login, get username, check if it exist in the file

elif choice == "2":
   username = input("Enter username:")
   password = input("Enter password: ")
   is_login = False
   f = open('userdata.txt','r')
   a = f.read()
   f.close()
   list_data = a.split(",")
   print(list_data)
   for i in list_data:
      z = i.split(":")
      if username == z[0] and password == z[1]:
         is_login = True
         
   if is_login:
      print("Login successfull")
   else:
      print("Invalid")

# Accounting- use file handling
# choice - login, register
# if register,get username, store the username in a file
# if login, get username, check if it exist in the file
