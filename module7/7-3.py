import string


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            words = []
            with open(file_name, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    line = line.translate(str.maketrans('', '', string.punctuation))
                    words.extend(line.split())
            all_words[file_name] = words
        return all_words

    def find(self, word):
        word = word.lower()
        all_words = self.get_all_words()

        result = {}
        for file_name, words in all_words.items():
            if word in words:
                result[file_name] = words.index(word) + 1  # Индексируем с 1 (чтобы не было 0)
        return result

    def count(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        result = {}
        for file_name, words in all_words.items():
            result[file_name] = words.count(word)  # Считаем количество вхождений
        return result


finder2 = WordsFinder('test_file.txt')

print(finder2.get_all_words()) # Все слова

print(finder2.find('TEXT')) # 3 слово по счёту

print(finder2.count('teXT')) # 4 слова teXT в тексте всего
