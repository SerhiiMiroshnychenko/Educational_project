import threading

def test(name):
    print(f'here {name}')


threads = []
for i in range(5):
    t = threading.Thread(target=test, args=(i,))
    threads.append(t)
    t.start()

for thread in threads:
    print(thread)
