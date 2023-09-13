"""
1 - Відкрити файл test_file.csv, прочитати його, зп співробітників у доларах перевести в гривні на поточну дату (курс задається окремою змінною). Результат зберегти новий файл salaries_uah.csv
"""


import csv

import os

exchange_rate = 37.8

root_folder = os.path.dirname(os.path.abspath(__file__))
input_file = 'test_file.csv'
output_file = 'salaries_uah.csv'
input_file_path = os.path.join(root_folder,input_file)
output_file_path = os.path.join(root_folder,output_file)

data = {}

with open (input_file_path, 'r' ) as f:
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
        employee_name = row[0]
        salaries_usd = [float(salary) for salary in row[1:]]
        salaries_uah = [round(salary * exchange_rate,2) for salary in salaries_usd]
        data[employee_name] = salaries_uah
        
with open (output_file_path, 'w', newline= '') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    for employee, salaries_uah in data.items():
        writer.writerow([employee] + salaries_uah)

with open (output_file_path, 'r', ) as f:
    for rows in csv.reader(f):
        print(rows)