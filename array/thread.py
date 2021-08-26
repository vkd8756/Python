from threading import *
from time import sleep
class A(Thread):
    def runs(self):
        for i in range(5):
            print("Hello")
            sleep(0.5)
            #print()
class B(Thread):
    def runs(self):
        for i in range(5):
            print("Hi")
            #print()
            sleep(0.5)
t1=A()
t2=B()
user=int(input("enter: "))
t1.start()
sleep(0.1)
t2.start()
t1.join()
t2.join()
print('bye')
