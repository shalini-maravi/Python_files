## Single Program of threding

""" class A():
    def run(self):
        for i in range(5):
            print('Akhilesh')
class B():
    def run(self):
        for i in range(5):
            print('viraj')
t1 = A()
t2 = B()

t1.run()
t2.run() """

## using sleep method

""" from time import sleep
class A():
    def run(self):
        for i in range(5):
            print('Akhilesh')
            sleep(1)
class B():
    def run(self):
        for i in range(5):
            print('viraj')
            sleep(1)
t1 = A()
t2 = B()

t1.run()
t2.run() """

## using Thread modulesfrom time import sleep from Threadig
""" from time import sleep
from threading import Thread
class A(Thread):
    def run(self):
        for i in range(5):
            print('Akhilesh')
            sleep(1)
class B(Thread):
    def run(self):
        for i in range(5):
            print('viraj')
            sleep(1)
t1 = A()
t2 = B()

t1.run()
t2.run() """

## using Thread modulesfrom time import sleep from Threadig
## All programming are compiler level execution
""" from threading import Thread
class A(Thread):
    def run(self):
        for i in range(5):
            print('Akhilesh')
            sleep(1)
class B(Thread):
    def run(self):
        for i in range(5):
            print('viraj')
            sleep(1)
# Print main
print('code')
t1 = A()
t2 = B()

t1.run()
t2.run() """

## Change the calling run() to start
from time import sleep
from threading import Thread
class A(Thread):
    def run(self):
        for i in range(5):
            print('Akhilesh')
            sleep(1)
class B(Thread):
    def run(self):
        for i in range(5):
            print('viraj')
            sleep(1)
# Print main
#print('code')
t1 = A()
t2 = B()
# Print main
print('code')
t1.start()  # Cpu Handel the Thread Auto-start
t2.start()  
# Print main
#print('code')
t1.join()  # legal Thread are first Execution
t2.join()  # legal Thread are first Execution