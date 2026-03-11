
# decorator - function vitra basey raw arko function lai call garna milchha decorator maah.

#def program(fun):
   # print("Inside program function")
   # fun()
   # print("program executed")
    
   # @program
  #  def peopel():
    #    print("Hellow world")
    
def swap(func):
       def inner(a,b):
        if b > a:
         a,b = b,a
         return func(a,b)
        return inner

@swap
def divide(a,b):
   return a/b

div = divide(2,10)
print(div)





# GiT - version control system.
 #     - used to track the changes.
 # Github - application based on GIT
 #        - used to store the projects.