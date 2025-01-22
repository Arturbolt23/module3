import random
import threading
import time



class Bank():

    def __init__(self, balance):
        self.ballance = int(balance)
        self.lock = threading.Lock()
        self.print_lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            ammount = random.randint(50, 500)
            self.ballance += ammount
            with self.print_lock:
                print(f' операция {i}, пополнение балланса на {ammount}, балланс: {self.ballance}')
            if self.ballance >= 500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.01)

    def take(self):
        for i in range(100):
            ammount = random.randint(50, 500)
            with self.print_lock:
                print(f'запрос на получение {ammount} руб.')
            if ammount <= self.ballance:
                self.ballance -= ammount
                with self.print_lock:
                    print(f'операция {i}, снятие {ammount}, остаток на счету : {self.ballance}')
            else:
                with self.print_lock:
                    print('запрос отклонен, недостаточно средств')
                self.lock.acquire()


bk = Bank(0)
th1 = threading.Thread(target=bk.deposit)
th2 = threading.Thread(target=bk.take)

th1.start()
th2.start()
th1.join()
th2.join()

print(f'итоговый балланс кошелька: {bk.ballance}')


