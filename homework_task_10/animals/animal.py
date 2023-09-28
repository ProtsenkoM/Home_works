from abc import ABC, abstractclassmethod, abstractmethod  # abstraction


class Animal(ABC):  # abstraction
    def __init__(self, name: str, species: str, age: int) -> None:
        self.name = name
        self.species = species
        self.age = age

    @abstractmethod  # abstraction
    def say_hello(self):
        pass

    @abstractmethod  # abstraction
    def give_birth(self):
        pass
