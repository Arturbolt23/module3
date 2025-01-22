import threading
counter = 0
lock = threading.Lock()
print(lock.locked())

def increement(name):
    global counter
    # lock.acquire()
    with lock:
        for i in range(1000):
            counter += 1
            print(name, counter)
    # lock.release()

def decreement(name):
    global counter

    try:
        lock.acquire()
        for i in range(1000):
            counter -= 1
            print(name, counter, lock.locked())
    except Exception:
        pass
    finally:
        lock.release()

thread1 = threading.Thread(target=increement, args= ('thread1',))
thread2 = threading.Thread(target=decreement, args= ('thread2',))
thread3 = threading.Thread(target=increement, args= ('thread3',))
thread4 = threading.Thread(target=decreement, args= ('thread4',))

thread1.start()
thread3.start()
thread2.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()
