import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    content = file.read().lower()  # Считываем содержимое и переводим в нижний регистр
                    for punct in string.punctuation + ' - ':  # Удаляем пунктуацию и тире
                        content = content.replace(punct, '')
                    
                    words = content.split()  # Разбиваем строку на слова
                    all_words[file_name] = words  # Добавляем в словарь
            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")
        
        return all_words

    def find(self, word):
        result = {}
        word = word.lower()  # Приводим к нижнему регистру для поиска
        all_words = self.get_all_words()
        
        for file_name, words in all_words.items():
            if word in words:
                result[file_name] = words.index(word) + 1  # +1 для получения позиции (с 1)
        
        return result

    def count(self, word):
        result = {}
        word = word.lower()  # Приводим к нижнему регистру для подсчета
        all_words = self.get_all_words()
        
        for file_name, words in all_words.items():
            result[file_name] = words.count(word)  # Подсчитываем количество вхождений
        
        return result

# Пример использования класса
finder2 = WordsFinder('test_file.txt')

# Получение всех слов
print(finder2.get_all_words())  # Все слова
# Поиск позиции слова
print(finder2.find('TEXT'))  # Позиция слова
# Подсчет количества вхождений
print(finder2.count('teXT'))  # Количество вхождений слова
