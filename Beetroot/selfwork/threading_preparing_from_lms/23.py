import threading

# l = threading.Lock()
l = threading.RLock()
print("before first acquire")
l.acquire()
print("before second acquire")
l.acquire()
print("acquired lock twice")
