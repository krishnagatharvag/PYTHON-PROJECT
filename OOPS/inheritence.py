"""
single inheritance
A..>>B


class father:
    def fat(self):
        print("this is father class")

class son(father):
    def sa(self):
        print("this is son class")


so=son()

so.fat()
so.sa()
"""

#multileval inheritance
#A..>>B..>>C
"""
class grandfather:
    def grand(self):
        print("this is grandfather class")

class father(grandfather):
    def fat(self):
        print("this is father class")

class son(father):
    def sa(self):
        print("this is son class")

so=son()
so.grand()
so.fat()
so.sa()
"""
"""

#multiple

class grandfather:
    def grand(self):
        print("this is grandfather class")

class father:
    def fat(self):
        print("this is father class")

class son(father,grandfather):
    def sa(self):
        print("this is son class")

so=son()
so.sa()
so.fat()
so.grand()
"""
#Hirerical
"""
class grandfather:
    def grand(self):
        print("this is grandfather class")

class father(grandfather):
    def fat(self):
        print("this is father class")

class son(grandfather):
    def sa(self):
        print("this is son class")

so=son()
so.sa()
so.grand()
fa=father()
fa.fat()
fa.grand()

"""
#hybride:combination of hirerical and multiple

class grandfather:
    def grand(self):
        print("this is grandfather class")

class father(grandfather):
    def fat(self):
        print("this is father class")

class son(grandfather):
    def sa(self):
        print("this is son class")

class cuson(father,son):
    def arpit(self):
        print("this is hybride class ")

cu=cuson()
cu.grand()
cu.fat()
cu.sa()
cu.arpit()