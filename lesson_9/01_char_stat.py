# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# TODO здесь ваш код

import zipfile as zf
from pprint import pprint

class StatCollector:
    def __init__(self, file_name, sort = 'by letter', reverse = False):
        self.file_name = file_name
        self.stat = {} # тут хранится инфа, сколько и каких символов существует в файле
        self.symbol_count = 0
        self.sort = sort
        self.reverse = reverse

    def unzip(self): 
        zip_file = zf.ZipFile(self.file_name, 'r')
        for packed_file in zip_file.namelist():
            zip_file.extract(packed_file)
        self.file_name = packed_file

    def engine(self):

        if self.file_name.endswith('.zip'):
            self.unzip()

        with open(self.file_name, 'r', encoding = 'cp1251') as file:
            for line in file:  # смотрим последовательно строки файла
                for char in line:  # смотрим последовательно символы в строке
                    if char in self.stat:  # проверяем, есть ли у нас уже статистика по символу
                        self.stat[char] += 1  # если да, то добавляем единичку к статистике
                    else:
                        self.stat.update({char:1})  # если нет, то создаем словарик для символа и вписываем первое появление символа
                    self.symbol_count += 1   # ведем подсчет общего числа символов в файле

        self.printer()

    def printer(self): 
        letters_count = 0

        print('Всего символов - ', self.symbol_count)

        print('+-----+----------+')
        print('|буква|количество|')
        print('+-----+----------+')

        if self.sort == 'by letter':  # сортировка по буквам
            for letter in sorted(self.stat, reverse=self.reverse): # пробегаем по сортированному по ключам словарю
                if letter.isalpha(): # выбираем только буквы
                    count = self.stat[letter] # выделено чисто длля удобства
                    print(f'|  {letter}  |  {count:6}  |')
                    letters_count += count # считаем сумму

        if self.sort == 'by count':  # сортировка по количеству
            for letter in sorted(self.stat, key=self.stat.get, reverse = self.reverse): # пробегаем по сортированному по количеству букв словарю         
                if letter.isalpha(): # выбираем только буквы
                   count = self.stat[letter] # выделено чисто длля удобства
                   print(f'|  {letter}  |  {count:6}  |')
                   letters_count += count # считаем сумму

        print('+-----+----------+')
        print(f'|итого| {letters_count}  |')
        print('+-----+----------+')
    
    #def printer_old(self):
    #    alph = [] # создаю пустй список alph
    #    char_code = ord('А')  # беру кодировку символа А большая 
    #    while char_code <= ord('я'):  # пробегаю по циклу до я малого
    #        alph.append(chr(char_code))  # дополняю список буквами
    #        char_code +=1 
    #    index_little_yo = alph.index('ж') # нахожу 
    #    alph.insert(index_little_yo, 'ё')  
    #    alph.insert(6, 'Ё')    # создал список букв алфавита в двух регистрах
    #    # без этого можно было обойтись, используя функцию isalpha, но тогда вывелась бы, в том числе, и статистика английского алфавита
    #    total_letters = 0
    #    print('+-----+----------+')
    #    print('|буква|количество|')
    #    print('+-----+----------+')
    #    for letter in alph:
    #        if letter in self.stat:
    #            letter_stat = self.stat[letter]
    #            print(f'|  {letter}  |  {letter_stat:6}  |')
    #            total_letters += letter_stat
    #    print('+-----+----------+')
        # но в общем и целом этот модуль printer_old - говнище, нужно оптимизировать


vim = StatCollector(file_name = 'C:\\Users\\Alex\\source\\repos\\lesson_9\\lesson_9\\voyna-i-mir.txt', sort = 'by count', reverse = True)

vim.engine()

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
