"""
1 - Відкрити файл test_file.csv, прочитати його, зп співробітників у доларах перевести в гривні на поточну дату (курс задається окремою змінною). Результат зберегти новий файл salaries_uah.csv
"""


import csv

exchange_rate = 37.8

with open ('homework_task_6/test_file.csv', 'r', ) as f:
    rows = csv.reader(f)
    new_list_of_employees = [row for row in rows]

with open ('homework_task_6/salaries_uah.csv', 'w', newline= '') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Salary (USD)', 'Salary (UAH)'])

    for employee in new_list_of_employees:
        name = employee[0]
        salary_usd = float(employee[1].replace('$', '').replace(',', ''))
        salary_uah = salary_usd * exchange_rate
        writer.writerow([name, f'${salary_usd:.3f}', f'{salary_uah:.3f}₴'])

with open ('homework_task_6/salaries_uah.csv', 'r', ) as f:
    for rows in csv.reader(f):
        print(rows)