
# polymorphism - euta class bataw many kaaam garaauney.

# Example -1
# a = 10
# b = 5
# print(a+b) 
# result 15 hunchha,
# Example - 2
 # a = 'x'
 # b = 'y'
 #print(x+y)
 # result xy
 
 # Example -1 and Example -2 ko result different way maa result garchha taraw garney tarika many ho.
 
 
 # Main Example - 3
class dog:
    def sound(self):
        print('Barking')
        
class Bird:
    def sound(self):
       print("Chriping")        
       
class cat:
    def sound(self):
        print("Meows")
        
obj1 = dog() 
obj2 = Bird()
obj3 = cat()  

obj1.sound()   
obj2.sound()  
obj3.sound()       