"""
2- Написати програму, яка просканує кореневу папку вашого проєкту, збереже у файл files_size.txt назви та розмір файлів, і надрукує назву найбільшого файлу та його розмір.
"""

import os

root_folder = '/Users/mihailprocenko/pythonproject/hilel_home_tasks/'

list_of_files = {}

with open ('homework_task_6/files_size.txt', 'w' ) as f:
    for foldername, subfolders, filenames in os.walk(root_folder):
        for filename in filenames:
            filepath = os.path.join(foldername, filename)
            filesize = os.path.getsize(filepath)
            f.write(f'{filepath}: {filesize} bytes\n')
            list_of_files[filepath] = filesize
if list_of_files:
    max_size = max(list_of_files.values())
    for key, value in list_of_files.items():
        if max_size == value:
            print (f'Найбільший файл: {key}')
            print (f'Розмір: {value} bytes')
else:
    print ('Папка порожня, або не вірний шлях до папки')
   




          


