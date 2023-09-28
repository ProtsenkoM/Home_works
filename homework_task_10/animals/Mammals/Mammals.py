from animals.animal import Animal


class Mammals(Animal):

    def __init__(self, name: str, species: str, age: int, Characteristic_Feature: str, Diet: str) -> None:
        super().__init__(name, species, age)
        self.Characteristic_Feature = Characteristic_Feature
        self.Diet = Diet

    def eat(self) -> None:
        print(f'{self.name} eats a {self.Diet}')

    def feature(self) -> None:
        print(f'{self.name} has the following {self.Characteristic_Feature}')

    def say_hello(self) -> None:
        print(f"{self.name} - say hello")

    def give_birth(self) -> None:
        print(f"New {self.name} was born")
