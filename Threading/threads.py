from time import sleep
from threading import *

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello Everyone ! 😊😊")
            sleep(1)
            
class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi Class! How's Going ;)")
            sleep(1)

task1 = Hello()
task2 = Hi()

task1.start()
sleep(0.1)
task2.start()

task1.join() #Main thread waits here for the two other threads to join
task2.join()
print("Done!")
