
from CustomIterator import CustomIterator

from Carriage import Carriage


class Train():
    def __init__(self, train_name: str, path: str) -> None:
        self.train_name = train_name
        self.path = path
        self.__cariage = []

    def add_cariage(self, cariage: Carriage):
        self.__cariage.append(cariage)

    def __len__(self):
        return len(self.__cariage)

    def __str__(self):
        train_string = "<=[HEAD]"
        for number_of_cariage in self.__cariage:
            train_string += f"-{number_of_cariage.number}"
        return train_string

    def __iter__(self):
        return CustomIterator(self.__cariage, 0, len(self.__cariage) - 1)

    def info(self):
        return self.train_name, self.path
