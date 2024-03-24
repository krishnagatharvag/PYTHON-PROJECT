"""
#astract class: astract classes are the class contain one or more abstract method
#astract method:astract method contain only defination no implementation
#we can not create object for abstract class
#we use astract class if we know the requirment but not know defination/implementation
#to use astract class we create subclass of astract class
"""

# from  abc import ABC,abstractclassmethod
# class A(ABC):
#     @abstractclassmethod
#     def display(cls):
#         None
#
# class B(A):
#     def display(self):
#
#         print("this is")
#
# mc=B()
# mc.display()
#
# from abc import ABC, abstractclassmethod
#
#
# class A(ABC):
#     @abstractclassmethod
#     def display(cls):
#         print("abstract method")
#
#
# class B(A):
#     def display(self):
#         super(B, self).display()
#         print("this is sub method")
#
#
# mc = B()
# mc.display()
from abc import ABC,abstractmethod
@abstractmethod
class A(ABC):
    def display(self):
        print("this is abstract method")


class B(A):
    def display(self):
        super(B, self).display()
        print("this is subclass")

mc=B()
mc.display()


