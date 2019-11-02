class A():
    def who(self):
        print("I am from A")
class B():
    def hello(self):
        print("I am from B")
class C(A,B):
  def c(self):
      print("I am from C")

d = C()  # d is a object of class C 
d.who() # a function from class A is called
d.hello() # a function from class B is called
