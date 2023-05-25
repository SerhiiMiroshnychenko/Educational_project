import threading

def greeting(name):
    print(f'{name} is here!')


thread_1 = threading.Thread(target=greeting, args=('Thread One',), name="Thread with Greeting")

thread_1.start()

print(f'Thread name is "{thread_1.name}"')
print(thread_1)
