#constructor is called as first function of the class
#constructor is used to initialized or assign values to the data member of the class
#we can decleare local variable to global, means we can use variable through the class
#it is executed when object of the class is created
#all the class having constructor by default
#constructor and method overloading is not allowed in python


               #constructor without parameter
class Practice:
    def __init__(self):
        print("inside constructor")


    def prac(self):
        print("outside constructor")


#pa=Practice()
pa=Practice()
pa.prac()

                 #constructor with parameter

class pracconst:

    def __init__(self,name,id):
        self.name=name
        self.id=id

    def prname(self):
        print("name is :{}, id is :{}".format(self.name,self.id))

co=pracconst("krishna",102)
print(co.name)
print(co.id)
co.prname()

                #constructor  overriding

"""
class Practice1:

    def __init__(self):
        print("base class")


class Chiled(Practice):

    def __init__(self):
        super(Chiled, self).__init__()
        print("chiled class")


ch=Chiled()
"""

class Practice:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b


    def display(self):
        print("this is method",self.a+self.b)

pa=Practice(5,6,7)#this is for constructor
pa.display()


class Practice:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        print(a+b+c)


    def display(self,x,y):
        print("this is method",self.a+self.b)
        print(x+y)

pa=Practice(5,6,7)#this is for constructor
pa.display(10,20)




