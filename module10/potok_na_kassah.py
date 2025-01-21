import threading
import time



class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name= str(name)
        self.power = int(power)
        self.life = 100


    def run(self):
        print(f'{self.name}, на нас напали!')
        counter = 1
        while self.life > 0:
            self.life -= self.power

            time.sleep(1)
            print(f'{self.name},сражается {counter} дня(день), осталось {self.life} воиеов.')
            counter += 1
        print(f'{self.name} одержал победу спустя {counter} дней!')

first_knight = Knight('Sir Lancelot', 10)
first_knight.start()

second_knight = Knight('Sir Galahad', 20)
second_knight.start()

first_knight.join()
second_knight.join()

print('все битвы закончились')
