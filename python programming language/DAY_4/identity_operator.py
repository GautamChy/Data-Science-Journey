
# identity - if memory location is same then output is True,otherwise false
a = 10
b = 10
print(a is b)
print(id(a))
print(id(b))

a = 15
b = 10
print(a is b)
print(id(a))
print(id(b))

# is not - if memory loction is same then output is false,otherwise True
a = 10
b = 10
print(a is  not b)
print(id(a))
print(id(b))

a = 15
b = 10
print(a is not b)
print(id(a))
print(id(b))
