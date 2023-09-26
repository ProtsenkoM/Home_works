"""1 -
Create a class describing any company. For example, Toshiba or Apple"""

from uuid import uuid4


class Company:

    def __init__(self, name_of_company: str, Founder: str, Annual_income: float, Head_office: str, Date_of_Incorporation: str, List_of_employees: int,
                 Industry: str, Financial_indicators: int, Contact_Information: str) -> None:
        """
        Конструктор класу Company, ініціалізує всі атрибути компанії.

        :param name_of_company: Назва компанії.
        :param Founder: Засновник компанії.
        :param Annual_income: Річний дохід компанії.
        :param Head_office: Місцезнаходження головного офісу компанії.
        :param Date_of_Incorporation: Дата заснування компанії.
        :param List_of_employees: Кількість співробітників компанії.
        :param Industry: Галузь, в якій працює компанія.
        :param Financial_indicators: Фінансові показники компанії.
        :param Contact_Information: Контактна інформація компанії.
        """
        self.name_of_company = name_of_company
        self.Founder = Founder
        self._Annual_income = Annual_income
        self.Head_office = Head_office
        self.Date_of_Incorporation = Date_of_Incorporation
        self.List_of_employees = List_of_employees
        self.Industry = Industry
        self.Financial_indicators = Financial_indicators
        self._Contact_Information = Contact_Information

    @property
    def Annual_income(self) -> float:
        """
        Звернення до річного дохіду компанії.
        :return: Річний дохід компанії.
        """
        return self._Annual_income

    @Annual_income.setter
    def Annual_income(self, new_annual_income) -> None:
        """
        Встановлення нового річного дохіду компанії.
        :param Annual_income: Річний дохід компанії.
        """
        if isinstance(new_annual_income, (int, float)):
            self._Annual_income = new_annual_income
        else:
            raise ValueError("Annual_income має бути числом")

    @property
    def Contact_Information(self) -> str:
        """
        Звернення до контактнаї інформація компанії.
        :return: Контактна інформація компанії.
        """
        return self._Contact_Information

    @Contact_Information.setter
    def Contact_Information(self, new_contact_Information) -> None:
        """
        Встановлення нової контактна інформація компанії.
        :param Contact_Information: Контактна інформація компанії.
        """
        self._Contact_Information = new_contact_Information

    def __str__(self) -> str:
        """
        Повертає рядок з інформацією про  компанію.
        :return: Рядок з інформацією про компанію.
        """
        return f"Company Name: {self.name_of_company}\nFounder: {self.Founder}\nAnnual Income: {self.Annual_income}\nIndustry: {self.Industry}"

    def __repr__(self) -> str:
        """
        Повертає рядок, що представляє об'єкт компанії.
        :return: Рядок, що представляє об'єкт компанії.
        """
        return f"Company({self.name_of_company}, {self.Founder}, {self.Annual_income}, {self.Head_office}, {self.Date_of_Incorporation}, {self.List_of_employees}, {self.Industry}, {self.Financial_indicators}, {self.Contact_Information})"

    @classmethod
    def create_startup(cls, name_of_company: str, Industry: str) -> 'Company':
        """Класс метод для створення нового стартапу як subbrand від компаннії.
        :param name_of_company: Назва стартапу.
        :param Industry: Галузь у якій буде працювати стартап
        :return: Обʼєкт стартапу(класс Company)
        """
        return cls(
            name_of_company=name_of_company,
            Founder="N/A",  # Значення N/A для засновника стартапу.
            Annual_income=0.0,  # По замовчуванню дохід дорівнює 0.
            Head_office="N/A",  # Значення "N/A" для головного офісу стартапу.
            # Значення "N/A" для дати заснування стартапу.
            Date_of_Incorporation="N/A",
            # По замовчуванню кількість співробітників стартапу дорівнює 0.
            List_of_employees=0,
            Industry=Industry,
            # По замовчуванню фінансові показники стартапу дорівнюють 0.
            Financial_indicators=0,
            Contact_Information="N/A"  # Значення "N/A для контактної інформації"
        )

    @staticmethod
    def generate_id() -> str:
        """Статичний метод для генерації унікального id

        :return: Унікальний ідентифікатор
        """
        return str(uuid4())


if __name__ == '__main__':
    Toshiba = Company(
        name_of_company="Toshiba Corporation",
        Founder="Tanaka Hisashige",
        Annual_income=158.94,
        Head_office="Minato, Tokyo, Japan",
        Date_of_Incorporation="11 July 1875",
        List_of_employees=116224,
        Industry="Technology",
        Financial_indicators=333697,
        Contact_Information="example@example.com"
    )
    print(str(Toshiba))
    print(repr(Toshiba))

    new_startup = Company.create_startup(
        name_of_company='New_startup',
        Industry='Tech'

    )
    print(str(new_startup))
    company_id = Company.generate_id()
    print(F"Company_id: {company_id}")

    print("Поточний річний дохід дорівнює:", Toshiba.Annual_income)
    Toshiba.Annual_income = 200.0
    print("Оновлений річний дохід:", Toshiba.Annual_income)

    print("Контактна інформація компанії:", Toshiba.Contact_Information)
    Toshiba.Contact_Information = 'mail@mail.com'
    print("Нова контактна:", Toshiba.Contact_Information)
    print(str(Toshiba))
  
