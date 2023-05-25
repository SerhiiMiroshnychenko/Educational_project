from threading import *
import time


s=Semaphore(2)

def wish(name,age):
  # for i in range(3):
  s.acquire()
  print("Hi",name, age)
  time.sleep(2)
  s.release()


t1=Thread(target=wish, args=("Sireesh",15))
t2=Thread(target=wish, args=("Nitya",20))
t3=Thread(target=wish, args=("Shiva",16))
t4=Thread(target=wish, args=("Ajay",25))

t1.start()
t2.start()

time.sleep(10)

t3.start()
t4.start()