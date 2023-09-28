from animals.Mammals.Cetaceans.Cetaceans import Cetaceans


class Delphinidae(Cetaceans):
    def __init__(self, name: str, species: str, age: int, Characteristic_Feature: str, Diet: str, habitat: str, migration_pattern: bool, vocalizations: bool, feeding_behavior: str) -> None:
        super().__init__(name, species, age, Characteristic_Feature,
                         Diet, habitat, migration_pattern)
        self.vocalizations = vocalizations
        self.feeding_behavior = feeding_behavior

    def swim(self):
        print(f"{self.name} is swimming gracefully in the water.")

    def jump(self):
        print(f"{self.name} jumps out of the water and performs a somersault.")

    def hunt(self):
        print(f"{self.name} is hunting for prey in the sea.")

    def socialize(self):
        print(f"{self.name} engages in social interactions with other dolphins.")

    def play(self):
        print(f"{self.name} is playing with seaweed and shells.")

    def get_description(self):
        return f"{self.name} is a {self.species} found in {self.habitat}. It has the following feeding behavior {self.feeding_behavior} and it can make sounds for communication {self.vocalizations}."
