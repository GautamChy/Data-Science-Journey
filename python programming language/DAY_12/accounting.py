
# Accounting- use file handling
# choice - login, register
# if register,get username and password, store the username in a file
# if login, get username and password, check if it exist in the file
# if user is valid then show them 2 options, 1,check balance, 2. add balance
# if option is add, ask for the amount to add and add it to the user's balance file {username:balance}
# if option is check, print the amount of the user if balance is present in the file, if not print "no balance"
# if user is not valid, print "invalid user"

def add_balance(username):
    f = open('balance.txt','a')
    add = input("Add amount ")
    f.write(f"{username}:{add}, ")
    f.close()
    
def check_balance(username):
    f = open('balance.txt','r')
    read = f.read().split(",")
    valid = False 
    initial = 0
    for i in read:
        z = i.split(":")
        if z[0] == username:
            valid = True
            initial += (z[1])
            
    if  valid :
        print(f"your balance is: {initial}")
    else:
      print("Not a valid")
     
     
    

def register():
    username = input("Enter your username: ")
    password = input("Enter your pasword: ")
    f = open('account.txt', 'a')
    f.write(f"{username}:{password},")
    print("Register successsful")
    f.close()
    
def login():
    username = input("Enter username:")
    password = input("Enter password: ")
    is_login = False
    f = open('userdata.txt','r')
    a = f.read()
    f.close()
    list_data = a.split(",")
    for i in list_data:
      z = i.split(":")
      if username == z[0] and password == z[1]:
         is_login = True
         
    if is_login:
        print("Login successful")
        c = input('''1.Add balance 
2.check balance ''')
        if c == '1':
            add_balance(username)
        elif c == '2':
            check_balance(username)
        else:
            print("invalid choice")
    else:
        print("inavlid")


choice = input('''1. Register
2. Login ''')
if choice == '1':
    register()
    
elif choice =='2':
    login()