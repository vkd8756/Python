class Animal:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def print_l(self):
        print(self.color,self.name)
class Cat(Animal):
    def say(self):
        print("meow")
a1=Animal("bruno","blue")
#print(a1)
#a1.print_l()
c1=Cat("ert","brown")
c1.print_l()
