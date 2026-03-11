
# inheritance - child class extends the attributes and methods of parent class 
   # i.e child class can use the attributes and methods that are present in parent class.
# syntax: class child_name(parent_class)
# child class have its own attributes and methods as well
# already existing methods in the parent class can be overridden in the child class.

# Requirments
# create a class named animal with attributes like legs, eyes, ear, methods like eat, sleep,....
# create a class named cat that inherits animal class, add other attributes like name, age.... and methods like sound
# create its objects

class animal:
    legs = None
    eyes = None
    ears = None
    
    def get_legs(self,legs):
        self.legs = legs
        
    def get_eyes(self,eyes):
        self.eyes = eyes 
        
    def get_ears(self,ears):
        self.ears = ears
        
    def get_eat(self,eat):
        self.eat = eat
        print(f"Animal is eating {self.eat}")
        
    def get_sleep(self,sleep):
        self.sleep = sleep
        print(f'Animal is {self.sleep}')    
            
obj1 = animal() 

obj1.get_legs('Animal have Four legs') 
print(obj1.legs) 
obj1.get_eyes('Animal have Two eyes') 
print(obj1.eyes) 
obj1.get_ears('Animal have Two ears') 
print(obj1.ears)

obj1.get_eat('bones')
obj1.get_sleep('sleeping')


class cat(animal):
    cat_name = None
    cat_age = None
    
    def get_cat_name(self,name):
        self.cat_name = name
        
    def get_cat_age(self,age):
        self.cat_age = age  
        
    def get_cat_sound(self,sound):
        self.cat_sound = sound
        print(f'cat sound is {self.cat_sound}')

obj2cat = cat()

obj2cat.get_legs('Cat have four legs')
print(obj2cat.legs)
obj2cat.get_eyes('Cat have two eyes')
print(obj2cat.eyes)
obj2cat.get_ears('Cat have two ears')

print(obj2cat.ears)
obj2cat.get_cat_name('Cat name is jessi')
print(obj2cat.cat_name)
obj2cat.get_cat_age('Cat age is three years')
print(obj2cat.cat_age)

obj2cat.get_cat_sound('meows')



    