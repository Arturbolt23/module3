import threading
import time


def func1():
    for i in range(10):
        time.sleep(1)
        print(i, threading.current_thread())

def func2():
    for i in range(10):
        time.sleep(.1)
        print(i, threading.current_thread())

thread = threading.Thread(target=func2)
thread.start()
# thread.join() ожидание выполнения всех потоков
time_start = time.time()
func1()
time_end = time.time()
print(time_end - time_start)
print(threading.current_thread())
print(thread.is_alive())
print(threading.enumerate())
print(threading.Thread().is_alive())
print()
