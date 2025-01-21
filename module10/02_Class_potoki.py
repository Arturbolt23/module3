import threading
import time
lock = threading.Lock()

class My_Thread(threading.Thread):
    def __init__(self, name, counter, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.counter = counter
        self.delay = delay

    def timer(self, name, counter, delay):
        while counter:
            time.sleep(delay)
            print(f' {name} {time.ctime(time.time())}')
            counter -= 1

    def run(self):
        print(f'поток {self.name} запущен')
        with lock:
            self.timer(self.name, self.counter, self.delay)
        print(f'поток {self.name} завершен')

thread1 = My_Thread('thread1', 5 , 1)
thread2 = My_Thread('thread2', 3 , 0.5)
thread1.start()
thread2.start()
