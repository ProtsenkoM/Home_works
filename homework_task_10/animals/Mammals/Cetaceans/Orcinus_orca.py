from animals.Mammals.Cetaceans.Cetaceans import Cetaceans


class Orcinus_orca(Cetaceans):
    def __init__(self, name: str, species: str, age: int, Characteristic_Feature: str, Diet: str, habitat: str, migration_pattern: bool, vocalizations: bool, feeding_behavior: str) -> None:
        super().__init__(name, species, age, Characteristic_Feature,
                         Diet, habitat, migration_pattern)
        self.vocalizations = vocalizations
        self.feeding_behavior = feeding_behavior

    def breach(self):
        print(f"{self.name} breaches out of the water with a spectacular jump!")

    def spy_hop(self):
        print(f"{self.name} performs a spy-hop to get a better view of the surroundings.")

    def hunt(self):
        print(f"{self.name} hunts down a school of fish with remarkable precision.")

    def protect_pod(self):
        print(f"{self.name} fiercely protects its pod members from potential threats.")

    def interact_with_marine_life(self):
        print(f"{self.name} interacts with various marine life, showcasing its intelligence and social behavior.")

    def get_description(self):
        return f"{self.name} is a {self.species} found in {self.habitat}. It has the following feeding behavior {self.feeding_behavior} and it can make sounds for communication {self.vocalizations}."
