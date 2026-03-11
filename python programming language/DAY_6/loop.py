
# Iteration - repeating the same task for multiple times.
# Loop - programming structure that implement iteration.Allowing a block of code to be executed multiples times.
# Two types of loop 1) while loop 2) for loop.
# while loop - conditional statement,if condition is True only then code inside the loop will be executed.
a = 0
b = 3
c = 5 

#while a < b :
     #print("Hellow world ")
     #a += 1               # a = 3
     #while c > b :
        #print("inside nested loop")
        #c -= 1
# break - used to terminate the loop and execute the next line.
#a = 0
#b = 3
#while a < b :
     #print(f"Hellow world {a} ")
     #a += 1  
     #if a == 3 :
        #break 
# continue - skip the current iteration and start a new iteration.
#a = 0
#b = 5
#while a < b :
    #if a == 2 : # 2 == 2 aayo vanney continue ley while condition chalaaidinchha talla na gaaikinna.
       # a += 1  
        #continue  
    #print(f"Hellow world {a} ")
    #a += 1  
     
# todo :
# # Calculator
# ask two number from user and store it in two veriable
# ask user to enter an operator (+, -, *, /) and store it in a veriable
# if the operator is +, add two number and print output
# if the operator is -, subtract two number and print output
# if the operator is *, multiply two number and print output
# if the operator is /, divide two number and print output
# ask user if they want to continue,if yes continue the calculation,
# if no end the program.

while True:
    inp_a = int(input("Enter first number: "))
    inp_b = int(input("Enter second number: "))

    op = input("Enter operator:(+/-/*/ /) ")

    if op == '+':
        res = inp_a + inp_b
        print(f"Sum : {res}")
    elif op == '-':
        res = inp_a - inp_b
        print(f"Difference : {res}")
    elif op == '*':
        res = inp_a * inp_b
        print(f"Product : {res}")
    elif op == '/':
        res = inp_a / inp_b
        print(f"Divide : {res}")
    else:
        print("Invalid operator")

    con = input("Do you want to continue?[y/n]: ")
    if con == 'y':
        continue
    elif con == 'n':
        break
    else:
        print("Wrong input!")
        break

# sessior, paper, rock
# there are two players
# ask player 1 (s,p,r)
# ask player 2 (s,p,r)
# if input of both player are same print tie
# if player 1 input is rock and player 2 input is paper, print player 2 wins
# if player 1 input is rock and player 2 input is sessior, print player 1 wins
# if player 1 input is paper and player 2 input is sessior, print player 2 wins

# ask if they want to continue, if yes continue the game, else exit the game

