class A():
    def who(self):
        print("I am from class A")
class B(A):
    def b(self):
        print("I am from B")

c = B() # c is an object of class B
c.who() # who function is called
#c.b()
