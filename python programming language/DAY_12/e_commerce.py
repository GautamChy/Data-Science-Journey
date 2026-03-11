
# ecommerce
# Register or Login
# choice - login, register
# if register,get username, password and usertype(buyer, seller), store the username in a file
# if login, get username and password, check if it exist in the file, login success if not invalid
# if user is a buyer: show them option: 1.View product, 2. buy product(billing option)
# if user is a seller: show them option: 1.View their product, 2.Add product(name, description, price) store it in a file 
# {
#   "name":"product1",
#   "description":"descrioion1",
#   "price":20,
#   "seller":"ram"
# },
# {
#   "name":"product2",
#   "description":"descrioion2",
#   "price":20,
#   "seller":"hari"
# }
import json

def register():
   username = input("Enter username:")
   password = input("Enter password")
   usertype = input("Enter usertype(b/s):")
   f = open('register.txt','a')
   a = {"username":username,"password":password,"usertype":usertype}
   json_a = json.dumps(a)   #dictinory is converted into json format
   f.write(f"{json_a}"+"-")
   print("Registation successfull")
   f.close()

def view_your_products(username):
   f = open('products.txt', 'r')
   r = f.read().split("-")
   for i in r:
      if i != '':
         json_product = json.loads(i)
         if json_product["seller"] == username:
            print(i)
   f.close()

def add_product(username):
   product_name = input('Enter product name: ')
   product_description = input('Enter product description: ')
   product_price = input('Enter product price: ')
   a = {
      "name":product_name,
      "description":product_description,
      "price":product_price,
      "seller":username}
   json_a = json.dumps(a)   #dictinory is converted into json format
   f = open('products.txt', 'a')
   f.write(json_a + "-")
   f.close()

def login():
   try:
      username = input("Enter username:")
      password = input("Enter password")
      is_login = False
      f = open('register.txt','r')
      a = f.read()
      f.close()
      list_data = a.split("-")
      for i in list_data:
         if i != '':
            dict_i = json.loads(i)   # converts json format into dictionary
            if dict_i.get("username") == username and dict_i.get("password") == password:
               print("Login success")
               is_login = True
               usertype = dict_i.get("usertype")
      
      if is_login:
         if usertype == "s":
            option = input('1.View Your Products\n2.Add Product\n>')
            if option == '1':
               view_your_products(username)
            elif option == '2':
               add_product(username)
         elif usertype == "b":
            pass
         
   except:
      print("No User Registered")

choice = input('''1. Register
2. Login''')

if choice == "1":
   register()

elif choice == "2":
   login()