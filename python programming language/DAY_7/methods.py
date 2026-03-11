

# string 
#a = "MINDRISERS"
#print(a.capitalize())
#print(a.casefold())
#print(a.count("I")) # count() maa data dinnu parchha

# list
#a = [1,2,3,'a',4,5]
#a.append('6') # kunai value list ma haldaa
#print(a)

#b = a.count(3) # 3 kati otaa chha,find out garchha,here its return so we have to store data in variable.
#print(b)

#a.insert(1,'Apple') # kunai value list maa haaldaa.
#print(a)

#print(a.pop(4))
#print(a)

# tuple
#a = (1,2,3,'a',4,5,'a')
#print(a.index(2)) # position show garchha
#print(a.index('a'))
#print(a.count('a'))

# set
#a = {1,2,3,4,5,6}
#b = {4,5,6,7,8,9}

#c = a.union(b)
#print(c)

#d = a.difference(b)
#print(d)

#e = b.difference(a)
#print(e)

#Dictionary
#a = {'name':'Gautam', 'age':20, 'city':'kathamdu'}
#print(a.items())
#print(a.keys())
#print(a.values())
#b = a.get('age') # value return garchha.
#print(b)

# task
# create a dictionary containing username and password,username as key and password as value.
# ask user for username and password
# check if the username and password are in the dictionary
# if yes print login success,else invalid cardentials.

a = {'Mindrisers':'123mindrisers'} # SEQUENTIAL ORDER VAAKO KAARANN MEMBERSHIP OPERATOR USE GARNA PAAYO EX- username in a
username = input("Enter your username: ")
password = input("Enter your password: ")
if username in a and a.get(username) == password: # username in a vanney ko user ley deko username chahee a maa chha ki nai.
    
    print("Login successful")
else:
    print("Invalid credentials")




