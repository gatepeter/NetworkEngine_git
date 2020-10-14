from threading import Thread
import time
def new():
   for x in range(6):
      print("Child Thread Here!!")
      time.sleep(1)

t1=Thread(target=new)
t1.start()
#t1.join()


print("Main Thread Here!!")

