class A():
    def who(self):
        print("I am from A")
class B(A):
    def who(self):
        print("I am from B")

c = B()
c.who()
