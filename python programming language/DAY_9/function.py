
# Function - like variable but instead of data,it store statement and it is reuseable.

#def function_name():     # function_name vitra statement store garyo.

    #print("Hellow world") # statement 
    #print("Hellow world") # statement 
    #print("Hellow world") # statement 
    #print("Hellow world") # statement 
    #print("Hellow world") # statement 
    
#function_name()           # function_name() yesto garey chee function_name vitra ko statement lai call garyo.

#..................................................................................................................

# parameter and arguments.
#name = "ram" 
#name1 = "shyam"
#name2 = "hari"

#def person(username): # () - parenthesis. parenthesis vitra raakhey ko variable lai parameter vanchha.eg- (username)
                        # username is a parameter and we also called variable so, variable vitra store garna milyo
    #print(username)
    
#person(name)
#person(name1)
#person(name2) # person() yo vaney ko function laii call garnu, name chaii username vitra store garyo,
                # yo vitra raakhey ko data lai argument vanchha so,name is an argument.
                
#.................................................................................................................. 

# positional argument or positional parameter - order anusaar data linchha.
# name = "ram" 
# name1 = "shyam"
# name2 = "hari"


# def person(username,age): # () - parenthesis. parenthesis vitra raakhey ko variable lai parameter vanchha.eg- (username)
                         # username is a parameter and we also called variable so, variable vitra store garna milyo
    # print(f"usename: {username}")
    # print(f"Age: {age}")
    
# person(name,"20") # name chahee username vitra store vayo and 20 chaii age vitra.
# person("20",name) # 20 chahee username vitra store vitra vayo and name chaii age vitra.
                  # jun position maa haaley ni sequencial order store hunchha.
#person(name1,"32")
#person(name2,"40")

#.....................................................................................................

# keyword argument or keyword parameter - parameter lai as a keyword liyeraw data lai assign garna milchha.
# name = "ram" 
# name1 = "shyam"
# name2 = "hari"

# def person(username,age):
#     print(f"username {username} ")
#     print(f"age {age}: ")
    
# person(username = name, age = "20") # username vitra name chaiyo and age vitra 20 chaiyo.
# person(age = "20", username = name) # username vitra name chaiyo and age vitra 20 chaiyo.

#............................................................................................................

# Default argument or positional parameter - 
# name = "ram" 
# name1 = "shyam"
# name2 = "hari"

# def person(username,age = 25):
#    print(f"username {username} ")
#    print(f"age {age}: ")
    
# person(name) 

#...........................................................................................................
# task 
# ask user for name, age, address,......
# create a function with parameters
# print out a introduction of the user function
# print introduction of 3 users

# name = input("Enter you name: ")
# age = input("Enter your age: ")
# address = input("Enter your address: ")

# def person(user_name,user_age,user_address):
#     print(f"My name is  {user_name} and my age is {user_age} and I am from {user_address}")
    
# person(name,age,address) 
 
 
 

#........................................................................................................

# ask user for 2 number
# crate a function that add two number given by user

# user = int(input("Enter number: "))
# user1 = int(input("Enter number: "))

# def addition(a,b): # a vaney ko variable ho So we have to store value, b vaney ko variable ho So we have to store value
#     c = a + b
#     print(f"Sum: {c}")
    
# addition(user,user1) 
   
