
# if else statement - multilined statement,  It is conditional statement,if condition is true only then statements inside  block are executed.
# if and elif are followed by condition, else is not followed by condition.
# elif can be defined by multiple times.
# statement inside else block is autamatically executed if the above condition is False.
# a = 10
# b = 5
# if a < b:
#     print(" A is smaller")
# else:                 # else maaa condition hudoina.
#     print(" A is greater") 
    
# a = 12
# b = 10
# if a < b: # condition follow gardai chha.
#     print(" A is smaller")
# elif a == b: # condition follow gardai chha.
#    print("A is equal to B ")
# elif a > b : # condition follow gardai chha.
#     print(" A is greater")
# else:                 # else maaa condition hudoina.
#     print(" Else statement") 
    

#Todo:
# ask user for their age
# if age is less than 18, print a statement (<)
# if age is gretaer than 18, print a statement(>)
# else,print a statement

user_age = input("Enter your age: ")
userr_age = int(user_age)
if userr_age < 18:
    print("You are not eligible for license")
elif userr_age > 18 :
    print("You are eligible for license")
else:
    print("User invalid")
    
    