
# exception handling - runtime errors
# the statement that may cause any errors are placed in the try block
# the statement that are executed incase any error are encountered are placed in except block.
# try block can have multiple except block
# ...................................................................................................
# try:
#  a = int(input("Enter number: "))
#  print(a)
# except ValueError:
#     print("ValueError")
# except NameError:
#     print("NameError")
# except:
#  print("Exception Block ")   
 
#...........................................................................................................
 
 # Calculator
# ask two number from user and store it in two veriable
# ask user to enter an operator (+, -, *, /) and store it in a veriable
# if the operator is +, add two number and print output
# if the operator is -, subtract two number and print output
# if the operator is *, multiply two number and print output
# if the operator is /, divide two number and print output 

while True:
 try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
 
    op = input("Enter operator (+, -, , /): ")

    if op == '+':
        print(f"Result: {a + b}")
    elif op == '-':
        print(f"Result: {a - b}")
    elif op == '':
        print(f"Result: {a * b}")
    elif op == '/':       
         print(f"Result: {a / b}")  
  
    else:
     print("Invalid operator.")       
 
 except ValueError:      # talla haalnu ko reason try: ley whole program ley handle garney vo and except programming vitra ko error lai handle garney vo.
  print("ValueError: Enter valid number")  

 choice = input("Do you want to continue (YES/NO): ").upper() # small yes type garey ni .uppee() ley capital maa convert gardinchha.
 if choice != 'YES' :  # YES bahek aru kehi type garyo vanney programm terminte garaidiney.
  break

 
  
  

#try:
 #a = int(input("Enter first number: "))
 #b = int(input("Enter second number: "))
 
#except ValueError:
 #print("ValueError")
#else:
 #op = input("Enter operator (+, -, , /): ")
 #if op == '+':
      #  print(f"Result: {a + b}")
 #elif op == '-':
 #       print(f"Result: {a - b}")
 #elif op == '':
  #      print(f"Result: {a * b}")
 #elif op == '/':
  #      try:
  #          print(f"Result: {a / b}")
   #     except ZeroDivisionError:
   #         print("ZeroDivisionError:  Impossible to divide any number by zero.")
 #else:
  #print("Invalid operator.")
       
# ...............................................................................................................
# ask user to enter a mark
# if mark is greater than 90 and less than 100,print Excellent
# if mark is greater than 80 and less than 90,print ....
# if mark is greater than 70 and less than 80,print ....
#if mark is greater than  60 and less than 70,print ....
#if mark is greater than  50 and less than 60,print ....
#if mark is greater than  40 and less than 50,print ....
#if mark is greater than  40,print ....

#try:
    #mark = int(input ("Enter your marks:"))
    #if 90 < mark <= 100 :
        #print("Excellent")
        
    #elif 80 < mark <= 90 :
     #print("Very Good ")
     
    #elif 70 < mark <= 80 :
     #print("Good ")
    
    #elif 60 < mark <= 70 :
     #print(" Average ")
     
    #elif 50 < mark <= 60 :
    # print(" Below Aveage")
    
   # elif 40 < mark < 50 :
    #    print("Pass")
       
    #elif mark< 40: 
   #    print("Fail ")
       
   # else:
    #    print("Out of range")       
       
#except ValueError :
   # print("ValueError: Enter valid number")   
    
 
        
                
