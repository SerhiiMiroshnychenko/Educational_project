from threading import *


l=RLock()

def factorial(n):
   l.acquire()
   result = 1 if n==0 else n*factorial(n-1)
   l.release()
   return result

def results(n):
   print("The Factorial of", n, "is:", factorial(n))


t1=Thread(target=results, args=(5,))
t2=Thread(target=results, args=(9,))

t1.start()
t2.start()
