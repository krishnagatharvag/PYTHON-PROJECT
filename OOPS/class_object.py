#class is a logical entity or blue print
#object is a physical entity of a class
#if we creat function within the class called method and outside class called function
"""
bydefault method inside the class is instance method,and if we mark @staticmethod then it become static so for staticmethod
no need to create object it is called directly by class name and self is not required in static
"""
"""
class Human():
    def eyes(self):
        pass


    def hairs(self,color):
        print(f"color of hair is  {color}")


ha=Human()
ha.hairs("black")
"""

"""
class Myclass():
    def inst(self):
        print("this is instance method")

    @staticmethod
    def stat():
        print("this is static method")

mc=Myclass()
mc.inst()
Myclass.stat()
"""

"""
#static method with parameter

class Myclass():
    def inst(self):
        print("this is instance method")

    @staticmethod
    def stat(value):
        print(value)


Myclass.stat(45)
"""
"""
#class variabls:
#if we have decleraed variables within the class called class variables and will be called by using self keyword


class Mathclass():
    a,b=10,20
    def add(self):
        print(self.a+self.b)


ma=Mathclass()
ma.add()
"""
"""
#accesing class variabls,local variabls,global variabls:
#if we have decleraed variables within the class called class variables and will be called by using self keyword
#if we have decleraed variables within the method called local variables and will be be called directly
#if we have decleraed variables otside class is called gloable variables and will be be called directly

i,j=5,15  #gloable variable
class Myclass():
    a,b=10,20  #class variable
    def add(self,x,y):  #x,y local variable
        print(self.a+self.b)
        print(x+y)
        print(i+j)


my=Myclass()
my.add(100,200)
"""
"""
#accesing local,globle,class variable by same name

a,b=5,15  #gloable variable
class Myclass():
    a,b=10,20  #class variable
    def add(self,a,b):  #x,y local variable
        print(self.a+self.b)
        print(a+b)
        print(globals()['a']+globals()['b'])


my=Myclass()
my.add(100,200)
"""

# a,b=5,10
# class Mathclass():
#     a,b=15,20
#     def myfunct(self,a,b):
#         print("this is local variable",a+b)
#         print("this is global variable",globals()['a']+globals()['b'])
#         print(f"this is class variable{self.a+self.b}")
#
#
# mat=Mathclass()
# mat.myfunct(25,30)

