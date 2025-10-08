##Function syntax with example
'''
def name():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    full_name =first_name + last_name
    print(full_name)
name()
'''

# addition of two numbers
#def digitadd(a,b):
 #   c=a+b
  #  print(c)
#digitadd(2,3) '''

# Function with the Return keyword
#def multi(c,d):
#    e=c*d
#    return e # With return alwasy use a variable that will store the result of function
#result=multi(10,20)# result is the variable that is storing the function value
#print(result)

#Passing a function as an argument
def add(a,b):
    return a+b
def square(c):
    return c*c
result=square(add(1,2))
print(result)





