"""
# many form of same thing called polymorphism,and same thing can behave differently based on the input we provide
#:button
#polymorphism can be achieved by method overriding and method overloading
"""
#method overloading-  two method having same name with different parameter in same class

#metod overrding-  two method having same name with same parameter in different class

"""
# overrding variables
class parent():
    name="scott"

class chiled(parent):
    #name = "david"
    pass

ca=chiled()
print(ca.name)
"""
"""
# overrding method
class Bank():
    def rate_of_interest(self):
        return 0


class Icici(Bank):
    def rate_of_interest(self):
        return 10.5


ic=Icici()
print(ic.rate_of_interest())
"""
"""

"""

#overriding using super keywords

# class Overbase():
#     def myname(self):
#         print("inside base class")
#
#
# class Overchiled(Overbase):
#     def myname(self):
#         super().myname()#by using super keyword we can access properties of parent class
#         print("inside chiled class")
#
#
# oc=Overchiled()
# oc.myname()

#overriding

class Myclass:
    def same(self,a,b):
        print("this is parent method",a+b)

class Second(Myclass):
    def same(self,a,b):
        super(Second, self).same(4,5)
        print("this is second method",a+b)


obj=Second()
obj.same(2,3)

"""

#overloading not possible

class Myclass:
    def first(self,a,b):
        print("this is first method",a+b)



    def first(self,a,b,c):
        print("this is second method",a+b+c)

obj=Myclass()
obj.first(1,2)

"""




#
# class Sbi:
#     def myname(self):
#         print("this is base class")
#
#
# class Icic(Sbi):
#     print("this is chiled class")
#
# ic=Icic()
# ic.myname()
#

"""

class Myclass:
    def first(self,a,b):
        print("this is first method",a+b)

class Second(Myclass)

    def first(self,a,b):
        super(Second, self).first(4,5)
        print("this is second method",a+b)

obj=Second()
obj.first(1,2)
"""


"""
class Myclass():
    def same(self):
        print("this is first class")

class Second(Myclass):
    def same(self):
        super(Second,self).same()
        print("this is second class")


ob=Second()
ob.same()
"""
















