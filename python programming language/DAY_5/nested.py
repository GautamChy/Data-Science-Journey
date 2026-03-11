
# nested 
#if codition:
    #statement
    #if condtion:
        #statement
    #elif condition :
        #statement  
        
 #elif condition:
     #statement
     #if condition
        #statement
    #elif condition:
       # statement
        
 #else:
     #statement
     # statement
    #elif condition:
        #statement
        
# a = 10
# b = 20
# c = 5
# if a < b : # yo if wala line correct vayo vanney matra talla walla if,else samma ko code start hunchha.
#     print("A is smaller than B") 
#     if a < c :
#      print("A is smaller than C ")
#     else:
#         print("A is greater than C")
# elif a > b :
#     print("A is greater than B ")
#     if b > c :
#         print("B is greater than C")
#     elif c < b :
#         print("C is smaller than B ")
# else:
#     print(" C is greater than B")
                             
   
 # ask user for their age
# if age is less than 18 print they are not eligible for licenses and
# ask if they any vehicle they want to get/buy then print some statement
# if age is greater or equal to 18 print they are eligible for licenses 
# and ask if they have any vehicle , if yes print a statement else print a statement  

user_age = int(input("Enter your age: "))

if user_age < 18:
    print("You are not eligible for lienses")
    a = input("Do you want to buy vehicle? (y/n)")
    if a == "y" :
        print("Yes")
    elif a == "n" :
        print("No")
    else:
        print("Neither y or n")   
elif user_age >= 18 :
    print(" You are eligible for license")  
    choice = input("Do you have any vehicle(y/n)")   
    if choice == "y" :
        print("Yes, I hav vehicle")  
    elif choice == "n":
          print("No,I don't have vehicle")
    else:
        print("Neither y or n ")      
        