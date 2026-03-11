
# Encapsulation - hiding data

# task
# create a class name account, it should have attribute username, account number, balance and methods to get the values for the attributes
# attributes should be private ,print out a statement that show the username and balance


class Account:
    __username = None
    __account_number = None
    __balance = None
    
    
    def get_show(self,name,blc):
        self.__username = name
        print(f'Usename is {self.__username}')
        self.__balance = blc
        print(f'balance is {self.__balance}')
    
    def private(self,number):
        self.__account_number = number
        print(f'Account number {self.__account_number}')
        
        
obj1 = Account()   
obj1.get_show('Ram','Rs 5000') 

obj1.private('1234')






    
    
    