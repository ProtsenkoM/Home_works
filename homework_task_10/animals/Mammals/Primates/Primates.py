from animals.Mammals.Mammals import Mammals


class Primates(Mammals):
    def __init__(self, name: str, species: str, age: int, Characteristic_Feature: str, Diet: str, tail: bool, climb_trees: bool) -> None:
        super().__init__(name, species, age, Characteristic_Feature, Diet)
        self.tail = tail
        self.climb_trees = climb_trees

    def has_tail(self):
        if self.tail:
            print(f"{self.name} has tail")
        else:
            print(f"{self.name} doesn't have tail")

    def can_climb_tress(self):
        if self.climb_trees:
            print(f"{self.name} can climb on tress")
        else:
            print(f"{self.name} can climb on tress")
