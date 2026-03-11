
# oop - Object oriented programming.
# inheritance
# polymorphism
# encapsulatiob
# abstraction

# class and object

# object - it is like a dictionary,if the data is created by the class is known as object

# class - structure,blueprint to create object

# attribute and methods in the class are accessed through object

# function and variable defined inside class are called methods and attribute respectively


#a = 'hello'
#print(type(a))

# Example 01
#class StudentForm: # student_form class ko name ho.class name  vitra ko variable lai attribute vanchh.ex- first_name,last_name,age
   # first_name = 'gautam'  #firs_name lai attribute vanchha.class vitra ko variable lai attribute vanchha.
    #last_name = 'chy'       # last_name lai attribute vanchha.class vitra ko variable  lai attribute vanchha.
   # age = 20  
    
#s1 = StudentForm()  #s1 is an object   # studentForm vitra ko laii call garn lai class name haalnu parchha.example - studentForm()        
#print(s1.first_name)        # s1 object ley call garyo attribute lai

# Example 02
#class StudentForm:
   # first_name = 'gautam' # variable vitra store garey ko lai static data vaninxa.ex- 'gautam'
   # last_name = 'chy' 
  #  age = 20 
    
#s1 = StudentForm()
#print(s1.first_name)
#s1.first_name = 'amrita'   
#print(s1.first_name)

# Example 03
#class StudentForm:
   # first_name = 'gautam' 
   # last_name = 'chy' 
  #  age = 20 
    
  #  def get_info(self,first_name):   # function lai oop maah method vanchha.class name vitra matra define garna milchha method lai.
  #   self.first = first_name    
  #   print(f"Firstname: {self.first}")
     
#s1 = StudentForm()

#s1.get_info("gopal")    # Gopal is dynamic      # s1 ley self linney vo. 


 #Example 03
#class StudentForm:
   # first_name = 'gautam' 
   # last_name = 'chy' 
   # age = 20 
    
    #def get_info(self):
       # print(f"Firstname: {self.first_name}")
        
        
    #def set_info(self, first_name):
     #   self.first_name = first_name
     #   self.get_info()               # arko method bataw arko method lai call garna milyo.
        
     
#s1 = StudentForm()
#s2 = StudentForm()


#s1.set_info("Gopal") 
#s2.set_info("ram")
   
# .....................................................................................................
# task
# Requierments
# create a class called dog
# should have attributes to define dog objects and methods like move, eat, get_legs, get_name

class Dog:
    dog_breed = 'German Shepherd'
    dog_color = 'brown and black'
    
    
    def get_name(self,dog_name):
        self.dog_name = dog_name
        print(f" Dog name is {self.dog_name}")
    
    def get_legs(self,dog_legs):
        self.dog_legs = dog_legs
        print(f" Dog has  {dog_legs} legs")
    
    def move(self,dog_move):
        self.dog_move = dog_move
        print(f" Dog move {self.dog_move}")
        
    def eat(self,dog_eat):
        self.dog_eat = dog_eat
        print(f" Dog eat {dog_eat}")
           
    
dog1 = Dog() 
  
dog1.get_name('rocky')
dog1.get_legs('four') 
dog1.move("Fast")
dog1.eat("bones")
print(f" Dog breed is {dog1.dog_breed}")
print(f" Dog color is {dog1.dog_color}")