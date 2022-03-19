# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# TODO здесь ваш код
class Parser:
    def __init__(self, events_file, combine_by = 'by minutes'):

        self.events = events_file
        self.comb = combine_by
        self.nok_count = 0
        #self.combine_edges = []

    def combiner(self):

        if self.comb == 'by minutes':
            self.right_edge = 17
        elif self.comb == 'by hours':
            self.right_edge = 14
        elif self.comb == 'by days':
            self.right_edge = 11
        elif self.comb == 'by months':
            self.right_edge = 8
        elif self.comb == 'by years':
            self.right_edge = 5

    def engine(self, stat_file):

        self.combiner()
        left = 0
        right = self.right_edge
        prev_str = 'start'

        events = open(self.events, 'r', encoding='cp1251')
        stats = open(stat_file, 'w', encoding='utf8')
        for string in events:
            if string.endswith('NOK\n'):
                if string[left:right] == prev_str:
                    self.nok_count += 1
                else:
                    if self.nok_count:
                        stats.write(f'{prev_str}] {self.nok_count}\n')
                    self.nok_count = 1  
                    prev_str = string[left:right]
        stats.write(f'{prev_str}] {self.nok_count}\n')
        events.close()
        stats.close()

fp = Parser('C:\\Users\\Alex\\source\\repos\\lesson_9\\lesson_9\\events.txt', 'by hours')
fp.engine('C:\\Users\\Alex\\source\\repos\\lesson_9\\lesson_9\\out.txt')

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828





# задача выполнена, есть нюанс - т.к. файл записи все время открыт, нельзя будет в середине процесса скопировать его и посмотреть результаты