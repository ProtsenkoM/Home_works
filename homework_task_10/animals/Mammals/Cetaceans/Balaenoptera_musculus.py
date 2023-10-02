from animals.Mammals.Cetaceans.Cetaceans import Cetaceans


class Balaenoptera_musculus(Cetaceans):
    def __init__(self, name: str, species: str, age: int, Characteristic_Feature: str, Diet: str, habitat: str, migration_pattern: bool, vocalizations: bool, feeding_behavior: str) -> None:
        super().__init__(name, species, age, Characteristic_Feature,
                         Diet, habitat, migration_pattern)
        self.vocalizations = vocalizations
        self.feeding_behavior = feeding_behavior

    def breach(self):
        print(f"{self.name} breaches above the water surface.")

    def find_food(self):
        print(f"{self.name} is searching for food.")

    def interact_with_humans(self):
        print(f"{self.name} interacts with humans during research.")

    def get_description(self):
        return f"{self.name} is a {self.species} found in {self.habitat}. It has the following feeding behavior {self.feeding_behavior} and it can make sounds for communication {self.vocalizations}."
