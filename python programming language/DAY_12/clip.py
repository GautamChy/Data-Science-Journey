
choice = input('''1.Register 
2. Login ''')
# if register,get username, store the username in a file
if choice == '1':
    username = input("Enter username: ")
    password = input("Enter your password:")
    f = open('userdata.txt','a')
    f.write(f"{username},")
    print("Registration succesful")
    f.close()
    
# if login, get username, check if it exist in the file
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
    