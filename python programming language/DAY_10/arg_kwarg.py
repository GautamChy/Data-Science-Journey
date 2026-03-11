
# global variable - jataa nee use garna paayo. return use garyo vanney function vitra ko print wala kaam rokk dinchha ani global banaaidinchha.
# local variable - variable defined inside a function,they can only be used inside that function.
 # Example :
#num = 50  # num = 50 is a global variable.
#def addition(a,b):  # a and b is a variable 
    #c = a + b       # c is a local variable.
   # return 
   # print(f"Sum: {c}")
    
#num1 = int(input("Enter number: "))
#num2 = int(input("Enter number: "))
    
#addition(num1,num2) # num1 and num2 ko value a and b variable maa store hunchha.

#print(num)

#....................................................................................................
# return - 
#def addition(num1,num2):
   # c = num1 + num2
    #return c     # return c ley feri value lai addition(a,b) mah send gardiyo.
    
#a =  int(input("Enter number: "))
#b =  int(input("Enter number:  "))
    
#sum = addition(a,b)  # return c ko value sum variable maah store garaidiyo.

#print(f"Global Sum :{sum}")  # suppose 2 + 2 = 4
#print(f"Global Multiply:{sum * 5}")  # 4 * 5 = 20 

#..............................................................
# return - end the function.i.e statement after return will not be executed.
#def addition(num1,num2):
   # c = num1 + num2
   # return c  
    #print("Hellow")        
    
#a =  int(input("Enter number: "))
#b =  int(input("Enter number:  "))
    
#sum = addition(a,b)  
#print(f"Global Sum :{sum}") 
#print(f"Global Multiply:{sum * 5}")  

#..........................................................................................
# return - function vitra ko statement print hunchha i.e return vanda mathi print hunchha.

#def addition(num1,num2):
   #  c = num1 + num2
   #  print("Hellow") 
   #  return c  
    
#a =  int(input("Enter number: "))
#b =  int(input("Enter number:  "))
    
#sum = addition(a,b)  
#print(f"Global Sum :{sum}") 
#print(f"Global Multiply:{sum * 5}")  

#..............................................................................................

# requirements - add the all the numbers that are provided to the function.
# Args - takes multiple data, '*' is used to define the args,tuple data type accept garchha.

# Example 1.
#def add(*args): # * yesko paxadee j name rakhey ni hunchha.
   # print(args)
    
#add(10,20,30,40,50,60,70,80,90,3,5,6,4,67,3,34,6,4,2,4,6,4,2,4,5,4,2,45,42,2,45,2,4,4)  

# Example-2.
#def add(*args): # * yesko paxadee jasto(eg-args) name rakhey ni hunchha.
   # print(args[3]) # kun position ko data chaiyo vanney [] use garney.
    
#add(10,20,30,40,50,60,70,80,90,3,5,6,4,67,3,34,6,4,2,4,6,4,2,4,5,4,2,45,42,2,45,2,4,4)  

# Example-3.
#def add(*abc) :
   # a = 0
   # for i in abc: # i = 1,3,2,4,5,6,7,4........
    #    a += i     #   a+= 1 vaney ko a= a+1 i.e 0+ 1= 1, 1+3=4, 4+2= 6, 6+4=10.......
   # print(a)

#add(1,3,2,4,5,6,7,4,3,56,4,3,4,5,4,3,4,4,)

#..............................................................................................................

# kwargs - takes multiple keyword argument,"**" is used to define kwargs. Dictionary data type accept garchha.

# example -1
#def person(**kwargs):
   # print(kwargs)
    
#person(name="Gautam",phonenumber= "986000125",email= "chygautam@gmail.com",address = "kathmandu")    

# Example -2 
#def person(**kwargs):
   # print(kwargs['email'])
    
#person(name="Gautam",phonenumber= "986000125",email= "chygautam@gmail.com",address = "kathmandu") 

# Example -3
#def person(**abc):
    #for key,value in abc.items():
     #print(f"{key}:{value}")
    
#person(name="Gautam",phonenumber= "986000125",email= "chygautam@gmail.com",address = "kathmandu") 