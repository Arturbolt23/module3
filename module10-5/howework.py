import time
import multiprocessing

# Функция для считывания информации из файла
def read_info(name):
    all_data = []  # Локальный список
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)

if __name__ == '__main__':
    # Создаем список файлов
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # Линейный вызов
    start_time = time.time()
    for file in filenames:
        read_info(file)
    end_time = time.time()
    print(f"Линейный вызов: {end_time - start_time:.6f} секунд")

    # Многопроцессный вызов
    start_time = time.time()
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        pool.map(read_info, filenames)
    end_time = time.time()
    print(f"Многопроцессный вызов: {end_time - start_time:.6f} секунд")
