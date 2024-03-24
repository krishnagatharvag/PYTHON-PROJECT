"""
encapsulation means we are wrapping our variable and method
encapsulation can be achieved by private method and variables
"""


"""
#private variales
#private variabl can be accessed only within the class
class Myclass():
    __a=10
    def myfu(self):
        print(self.__a)

mc=Myclass()
mc.myfu()
"""
#private method
#private method can be accessed only within the class

class Myclass():
    def __disp1(self):
        print("this is first method")

    def disp2(self):
        #print("this is second method")
        self.__disp1()

mc=Myclass()
mc.disp2()




class Encap:
    def __display_1(self,a,b):
        print("this is first method",a+b)


    def display_2(self,c,d):
        print("this is second method",c*d)
        self.__display_1(2,3)

obj=Encap()
obj.display_2(3,4)
