"""2 -
Create a class with a description of the worker. Any worker or employees."""


"""не забути додати анотації, c статичні методи, гетери та сетери, класс методи, додати секьюрність, класс метод"""


class Employee:

    company = 'Apple'  # attr of class

    def __init__(self, name: str, age: int, salary: int, employee_id: int, department: str, job_position: str,
                 birthday_date: str) -> None:
        """
        Конструктор класу Employee, ініціалізує всі поля співробітника.

        :param name: Ім'я співробітника.
        :param age: Вік співробітника.
        :param salary: Зарплата співробітника.
        :param employee_id: Ідентифікатор співробітника.
        :param department: Департамент, в якому працює співробітник.
        :param job_position: Посада співробітника.
        :param birthday_date: Дата народження співробітника.
        """
        self._name = name
        self.age = age
        self.__salary = salary
        self.employee_id = employee_id
        self.department = department
        self.__job_position = job_position
        self.address = []
        self.birthday_date = birthday_date
        self.__personal_security_data = {}

    @property
    def salary(self) -> int:
        """
        Звернення до зарплати співробітника.

        :return: Зарплата співробітника.
        """
        return self.__salary

    @salary.setter
    def salary(self, new_salary) -> None:
        """
        Встановлення нового значення зарплати співробітника.

        :param new_salary: Нова зарплата співробітника.
        """
        self.__salary = new_salary

    def add_address(self, new_address) -> None:
        """
        Додавання адреси співробітника.

        :param new_address: Нова адреса співробітника.
        """
        self.address.append(new_address)

    @property
    def job_position(self) -> str:
        """
        Звернення до посади співробітника.

        :return: Посада співробітника.
        """
        return self.__job_position

    @job_position.setter
    def job_position(self, new_job_postion) -> None:
        """
        Встановлення нової посади співробітника.

        :param new_job_position: Нова посада співробітника.
        """
        self.__job_position = new_job_postion

    def add_personal_security_data(self, new_financial_security_data) -> None:
        """
        Додавання особистих даних співробітника.

        :param new_personal_security_data: Нові особисті дані у вигляді словника.
        """
        for key, value in new_financial_security_data.items():
            self.__personal_security_data[key] = value

    def get_personal_security_data(self, key: str):
        """
        Отримання особистих даних співробітника за ключем.

        :param key: Ключ для отримання конкретного поля особистих даних або 'all' для отримання всіх даних.
        :return: Особисті дані співробітника або 'Not found', якщо ключ не існує.
        """

        for k, v in self.__personal_security_data.items():
            if k == key:
                return self.__personal_security_data.get(k)
            elif key == 'all':
                return self.__personal_security_data

    def __str__(self) -> str:
        """
        Повертає рядок з інформацією про співробітника.

        :return: Рядок з інформацією про співробітника.
        """
        return f"Employee Name: {self.name}\nEmployee ID: {self.employee_id}\nDepartment: {self.department}\nPosition: {self.job_position}\nSalary: {self.salary}"

    def __repr__(self) -> str:
        """
        Повертає рядок-представлення об'єкта Employee.

        :return: Рядок-представлення об'єкта Employee.
        """
        return f"Employee('{self.name}', {self.age}, {self.salary}, {self.employee_id}, '{self.department}', '{self.job_position}', '{self.birthday_date}')"

    def _do_welcome(self):
        print(f'{self.name} says - welcome to new job')

    def do_work(self):
        self._do_welcome()

    @staticmethod
    def company_info():
        """
        Статичний метод, що повертає інформацію про компанію.
        """
        return f"This is {Employee.company}."

    @classmethod
    def change_company_name(cls, new_name) -> None:
        """Метод класу для зміни назви компанії
        """
        cls.company = new_name


if __name__ == '__main__':
    Mike = Employee('Mike', 34, 2000, 12345, 'QA', 'Manual QA', '09.08.2000')
    print(str(Mike))
    Mike.add_address("city: Sumy, Addr: 15 avenue street, apt 15")
    print(Mike.address)
    Mike.add_personal_security_data(
        {'cell_number': 380500000001, 'email': 'mail@mail.com', 'card_number': '12332432412123'})
    print(Mike.get_personal_security_data('cell_number'))
    print(Mike.get_personal_security_data('all'))
    print(repr(Mike))
    Mike.do_work()
    company_info = Mike.company_info()
    print(company_info)
    Employee.change_company_name('Google')
    print(f'Company was change to {Employee.company}')
    print(Mike.company)
    print("Поточна зарпала:", Mike.salary)
    Mike.salary = 3000
    print("Нова зарплата:", Mike.salary)
    print(str(Mike))
