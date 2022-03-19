# -*- coding: utf-8 -*-

import os, time, shutil
import zipfile as zf

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# TODO здесь ваш код

class Catalogiser:

    def __init__(self, initial_file, result_folder):  # инициализация раскладчика с исходным файлом и целевой папкой
        self.initial_file = initial_file
        self.result_folder = result_folder

    def unpack(self):  # распаковка файла если он зазипован, проверяется на зазипованность файл не здесь, а в модуле engine
        zfile = zf.ZipFile(self.initial_file, 'r')
        for pfile in zfile.namelist():
            zfile.extract(pfile)
        self.initial_file = self.initial_file.replace('.zip', '')
      
    def engine_start(self):

        if self.initial_file.endswith('.zip'):
            self.unpack()

        for dirpath, dirnames, filenames in os.walk(self.initial_file):
            for file in filenames:
                file_path = os.path.join(dirpath, file)
                secs = os.path.getmtime(file_path)  # возраст файла с начала эпохи
                file_created = time.gmtime(secs)  # переводим в UTC
                #file_put = self.result_folder + '\\' + file_created[0] + '\\' + file_created[1] + '\\' + file
                file_put = f'{self.result_folder}\\{file_created[0]}\\{file_created[1]}'
                os.makedirs(name = file_put, exist_ok = True)
                file_put += f'\\{file}'
                shutil.copy2(src = file_path, dst = file_put)
                #print(file_path, end = ' ')
                #print(file_created)

    def engine_for_not_packed(self):
        pass


current_path = os.path.abspath(__file__)  # получаем путь к исп. файлу
current_path = os.path.split(current_path)[0]  # берем только путь к директории
init_path = current_path + '\\icons.zip'
res_path = current_path + '\\catalogised'
icat = Catalogiser(init_path, res_path)
icat.engine_start()

# эту | усложненку делать не буду, но, может, потом сделаю распаковку внутренних архивов (рюкзак в рюкзак, привет, Тарков)
#     V

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
