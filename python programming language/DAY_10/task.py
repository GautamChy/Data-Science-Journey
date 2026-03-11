
# Calculator by using function
# ask two number from user and store it in two veriable
# ask user to enter an operator (+, -, *, /) and store it in a veriable
# if the operator is +, add two number and print output
# if the operator is -, subtract two number and print output
# if the operator is *, multiply two number and print output
# if the operator is /, divide two number and print output

while True:
  def add(num1,num2):
   c = num1 + num2
   return c

  def sub(num1,num2):
    c = num1 - num2
    return c

  def mult(num1,num2):
    c = num1 * num2
    return c

  def div(num1,num2):
    c = num1 / num2
    return c

  a = int(input("Enter first number: "))
  b = int(input("Enter second number: "))

  op = input("Enter an operator(+,-,*,/)")

  if op == "+" :
   sum= add(a,b)
   print(f"Addition: {sum}")
    
    
  elif op == "-" :
     subtraction = sub(a,b)
     print(f"subtraction: {subtraction}")
      
  elif op == "*" :
   multiply = mult(a,b)
   print(f"Multiply: {multiply}")
    
  elif op == "/" :
     division= div(a,b)
     print(f"Division: {division}")
    
  else:
    print("Invalid operator")   
    
  choice = input(" Do you want to continue(Y/N)").upper()    
  if choice != "Y":
     break
        
           
        