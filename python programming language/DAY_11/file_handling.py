
# open a file,
# open('path of file','mode')
# r - to open file in read mode
# example
# a = open('file.txt','r')
# b = a.read()
# print(b)

# write 'w' to open file  data in a file,create a file if it does not exit in the location,data overridden.
# example 
# a = open('file.txt','w')
# a.write("my name is gautam")

 # store the new data with the old data by using append 'a'
 #  example
#a = open('/Users/maclap.in/Desktop/Chaitra/DAY_11/file.txt','a') 
#a.write(" world")


# task
#choice - login, register
choice = input('''1.Register 
# 2. Login ''')
# # if register,get username, store the username in a file
if choice == '1':
    username = input("Enter username: ")
    f = open('userdata.txt','a')
    f.write(f"{username},")
    print("Registration succesful")
    f.close()
    
# # # if login, get username, check if it exist in the file
elif choice == '2' :
    username = input("Enter username: ")
    f = open('userdata.txt','r')
    a = f.read()
    f.close()
    list_data = a.split(",")
    for i in list_data :
        print(i)
        if username == i :
            print("Login success")
            break
        else:
            print("Login failed")
            break
    