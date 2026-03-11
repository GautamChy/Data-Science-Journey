
# Accounting by using function
# create a dictionary that stores user data
# create another dictionary that stores user name and balance, username as key and balance as value
# ask user for their credientials
# if user is valid then show them 3 options, 1,check balance, 2. add balance, 3. withdraw balance
# if option is check, print the amount of the user
# if option is add, ask for the amount to add and add it to the user's balance
# if option is withdraw, ask for the amount to withdraw, check if the withdraw amount is less than the balance, 
# if the withdraw amount is less than the balance, subtract the withdraw amount from the balance, 
# else print "insufficient balance"
# if user is not valid, print "invalid user"

userdata = {"Gautam":"password123" , "ram":"ram123" , "shyam":"shyam123" }

account = {"Gautam":"1000" , "ram":"1500" , "shyam": "10000"}

username = input("Enter your username: ")
password = input("Enter your password: ")

if username in userdata and userdata.get(username) == password :
    print("valid user")
    
    choice = input('''1. check balance
2. add balance
3. withdraw balance>>> ''')
    
    if choice == "1" :
     print(f"Your balance is : {account.get(username)}")
     
    elif choice == "2" :
        add = int(input("Enter amount: "))
        balance = account.get(username)
        total = add + balance 
        print("f your total balance is : {total}")
        
    elif choice == "3" :
         withdraw = int(input("Withdraw amount: "))
         balance = account.get(username)
         if withdraw < balance :
             total = withdraw - balance
             print("f your balance is : {total}")
             
         else:
             ("Insufficient balance")

else:
    print("Invalid users")             
        
        