import time
import threading


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(1, word_count + 1):
            f.write(f'какое то слово № {i}\n')
            time.sleep(0.1)
    print(f'завершилась запись в файл {file_name}')

def measure_function_time(func, *args):
    start_time = time.time()
    func(*args)
    end_time = time.time()
    return end_time - start_time

def measure_thread_time():
    threads = []
    filenames = [
        ('example5.txt', 10),
        ('example6.txt', 30),
        ('example7.txt', 200),
        ('example8.txt', 100)
        ]
    for filename, word_count in filenames:
        thread = threading.Thread(target=write_words, args=(word_count, filename))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    start_time = time.time()
    write_words(10, 'example1.txt')
    write_words(30, 'example2.txt')
    write_words(200, 'example3.txt')
    write_words(100, 'example4.txt')
    end_time = time.time()
    print(f'работы функций {end_time - start_time} секунд')

    start_time_threads = time.time()
    measure_thread_time()
    end_time_threads = time.time()
    print(f'работа потоков {end_time_threads - start_time_threads} секунд')
