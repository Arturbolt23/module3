import random
import time
from threading import Thread
from queue import Queue

class Table:
    def __init__(self, number, guest=None):
        self.number = number  # Номер стола
        self.guest = guest    # Гость за столом (по умолчанию None)

class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name      # Имя гостя

    def run(self):
        time.sleep(random.randint(3, 10))

class Cafe:
    def __init__(self, *tables):
        self.tables = tables  # Список столов
        self.queue = Queue()  # Очередь для гостей

    def guest_arrival(self, *guests):
        for guest in guests:
            assigned_table = None
            # Пытаемся посадить гостя за первый свободный стол
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest  # Сажаем гостя за стол
                    assigned_table = table
                    print(f"{guest.name} сел(-а) за стол номер {table.number}")
                    guest.start()  # Запускаем поток для гостя
                    break

            if assigned_table is None:
                # Если нет свободных столов, гость идет в очередь
                self.queue.put(guest)
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        # Обслуживание гостей
        while not self.queue.empty() or any(table.guest is not None and table.guest.is_alive() for table in self.tables):
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    # Гость покушал и ушел
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None  # Освобождаем стол

                # Если есть свободный стол и очередь не пуста, сажаем следующего гостя
                if table.guest is None and not self.queue.empty():
                    guest = self.queue.get()
                    table.guest = guest
                    print(f"{guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
                    guest.start()  # Запускаем поток для нового гостя

            time.sleep(1)  # Задержка, чтобы избежать слишком частых проверок

# Создание столов
tables = [Table(number) for number in range(1, 6)]

guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]


guests = [Guest(name) for name in guests_names]


cafe = Cafe(*tables)


cafe.guest_arrival(*guests)


cafe.discuss_guests()
