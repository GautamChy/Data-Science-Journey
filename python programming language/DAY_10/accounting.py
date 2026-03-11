
# Accounting
# create a dictionary that stores user data
userdata = {"Gautam":"password123",  "ram":"ram123",  "hari":"hari123",  "shyam":"shyam123"}
# create another dictionary that stores user name and balance, username as key and balance as value
account = {"Gautam":10000,  "ram":15000,  "hari":19000,  "shyam":45000}
# ask user for their username and password  credientials
username = input("Enter your username: ")
password = input("Enter password: ")
# if user is valid then show them 3 options, 1,check balance, 2. add balance, 3. withdraw balance
if username in userdata and userdata.get(username) == password :   # (username) is a key.
    print("Valid user")
    
    
    choice = input('''1.check balance 
  2.add balance 
  3.withdraw balance >>>  ''')
# if option is check, print the amount of the user
if choice == '1':
        print(f"Your balance is: {account.get(username)}")
        
# if option is add, ask for the amount to add and add it to the user's balance
elif choice == '2' : 
        add =int(input("Add amount: "))
        balance = account.get(username)
        total = add + balance
        print(f"Your new balance is: {total}")
# if option is withdraw, ask for the amount to withdraw, check if the withdraw amount is less than the balance,
# if the withdraw amount is less than the balance, subtract the withdraw amount from the balance, else print "insufficient balance"
# if user is not valid, print "invalid user"
elif choice =='3' :
        withdraw = int(input("Amount to withdraw: "))
        balance = account.get(username)
        if withdraw < balance:
           total = balance - withdraw
           print(f"Your new balance is :{total}")
        
        else:
         print("Insufficent balance")
 
 
else:
    print("Invalid users")  
    


    





 

    
        
    
    
    
     
    
 
    
    # BY USING FUNCTION
    # Accounting
# create a dictionary that stores user data
# create another dictionary that stores user name and balance, username as key 
# and balance as value
# ask user for their credientials
# if user is valid then show them 3 options, 1,check balance, 2. add balance, 3. withdraw balance
# if option is check, print the amount of the user
# if option is add, ask for the amount to add and add it to the user's balance
# if option is withdraw, ask for the amount to withdraw, check if the withdraw amount 
# is less than the balance, if the withdraw amount is less than the balance, subtract 
# the withdraw amount from the balance, else print "insufficient balance"
# if user is not valid, print "invalid user"

#user_data = {'ram': 'ram123', 'hari': 'hari123', 'u':'u'}
#account = {'ram': 10000, 'hari': 900000, 'u':890000}

#username = input(('Enter your username: '))
#password = input(('Enter your password: '))

#def show_balance(username):
  #  return account.get(username)

#def add_balance(username, amt):
  #  add_amt = account.get(username)
  #  new_balance = add_amt + amt
  #  return new_balance

#def wit_balance(username, amt):
   # initial_balance = account.get(username)
   # new_balance = initial_balance - amt
   # return new_balance

# Check if the username is in database
#if username in user_data:
    # Check if the passwords match
   # if user_data.get(username) == password:
    #    print('LOGGED IN')
    #    while True:
     #       choice = input('''
#****Welcome to your account!***
#1. Check balance
#2. Add balance
#3. Withdraw balance
#>
#''')        
            # Catch error for wrong input to int values 
 #           try:
  #              if choice == '1':
   #                 # Calling relevant functions
    #                print(f'Your balance is: {show_balance(username)}')
     #           elif choice == '2':
      #              add_amt = int(input('Enter your amount to add to your account: '))
       #
       # wit_amt = int(input('Enter your amount to withdraw from your account: '))
                    # Checking if the amount entered can be withdrawn
         #           if account.get(username) >= wit_amt:
          #              print(f'Your new balance is: {wit_balance(username, wit_amt)}')
           #         else:
            #            print('Insufficient Balance!')
             #   else:
              #      print('Invalid input!')
           # except:
           #     print('Enter number value to be added!')

           # choice = input('Do you want to keep using the app?[y/n]: ').upper()
           # if choice != 'Y':
          #      break
   # else:
    #    print('Password doesn\'t match to username!')
#else:
  #  print('Username doesn\'t exists')                                                              
    


