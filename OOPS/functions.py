# function is a peace of code written in a block to reuse: eg. print()
# fuction with parameter fuction without parameter
# collection of multiple function creats programme
# predefined function print(),short(),add(),math(),choice(),shuffle(),count(),round()
"""
def my_name_is():
    # print("my name is krish")
    return "my name is krish1"


# my_name_is()
print(my_name_is())


def my_son_name_is(name):#name parameter
    # print("my son name is",name)
    return "my son name is " + name


# my_son_name_is("Atharva")#atharva argument
print(my_son_name_is("Atharva1"))


def country_name(cname):
    print(f"country name is {cname}")


country_name("india")


def get_user_details(name, age, salary):
    # print(f"name is :{name} age is :{age} salary is:{salary}")
    print("name is", name, "age is", age, "salary is", salary)


get_user_details("krish", 37, 1000000)
"""
"""
def new_function():
    result=3*2
    return result

out=new_function()
print(out)

print(f"This is the output of new_function is :{out}")

"""
"""
def new_function():
    return 3*2

new_function()
print(f"This is the output of new_function is :{new_function()}")

# def new_function(a,b):
#     return a*b
# 
# print(f"This is the output of new_function is :{new_function(2,4)}")

"""

# def formate_name(f_name,l_name):
#     out1=f_name.title()
#     out2=l_name.title()
#     print(f"my first name:{out1}, and last name:{out2}")
#
# formate_name("krishna","goswami")


#
# def formate_name(f_name,l_name):
#     out1=f_name.title()
#     out2=l_name.title()
#     return f"my first name:{out1}, and last name:{out2}"
#
# print(formate_name("krishna","goswami"))
# new_output=formate_name("krishna","goswami")


"""
#return tells the computer that this is the end of function
def formate_name(f_name,l_name):
    out1=f_name.title()
    out2=l_name.title()
    return f"my first name:{out1}, and last name:{out2}"
    print("after the return")#this ststment will not be executed becuse return means end of function

print(formate_name("krishna","goswami"))
new_output=formate_name("krishna","goswami")
print(new_output)
"""




"""
#multiple return

def formate_name(f_name,l_name):
    if f_name=="" or l_name=="":
        return "you did not enter frist name or last name" #return means end of the programme
    out1=f_name.title()
    out2=l_name.title()
    return f"my first name:{out1}, and last name:{out2}"

print(formate_name(input("Enter first name"),input("Enter last name")))#enter nothing in console
"""
"""
#calculater function
def addi(n1,n2):
    return n2+n1

def subtrac(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2
num1=eval(input("Enter first number"))

oprtation={"+":addi,
           "-":subtrac,
           "*":multiply,
           "/":div}

for symbol in oprtation:
    print(symbol)
operat_symbol=input("Pick a symbol out of the option given above")
num2=eval(input('Enter second number'))

calculate_function=oprtation[operat_symbol]
answer=calculate_function(num1,num2)
print(f"{num1} {operat_symbol} {num2} = {calculate_function(num1,num2)}")
print(f"{num1} {operat_symbol} {num2} = {answer}")
"""
"""
#print vs return: if we using output of firdt function to unput for another function, then print will not work
#only retun will work in this condition
# def frist_function(a,b):
#     return a+b
#
# first_output=frist_function(2,4)
#
# def second_function(x):
#     return first_output*5
#
# print(second_function(5))

def frist_function(a,b):
    print(a+b) 

first_output=frist_function(2,4)

def second_function(x):
    return first_output*5

print(second_function(5))

"""
"""
#while loop with flag and recursion

def addi(n1,n2):
    return n2+n1

def subtrac(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2
def calculator():
    num1=eval(input("Enter first number"))

    oprtation={"+":addi,
               "-":subtrac,
               "*":multiply,
               "/":div}

    for symbol in oprtation:
        print(symbol)

    should_contineu=True

    while should_contineu:
        operation_symbol=input("Pick operation from avobe")
        num2=eval(input("Enter second number"))
        calculation_function=oprtation[operation_symbol]
        ansewr=calculation_function(num1,num2)
        print(f"{num1}+{num2}={ansewr}")
        if input(f"enter y to continew or n to to start again")=='y':
            num1=ansewr
        else:
            should_contineu = False
            calculator()


calculator()
"""


