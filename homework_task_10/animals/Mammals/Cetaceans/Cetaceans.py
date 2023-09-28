from animals.Mammals.Mammals import Mammals


class Cetaceans(Mammals):
    def __init__(self, name: str, species: str, age: int, Characteristic_Feature: str, Diet: str, habitat: str, migration_pattern: bool) -> None:
        super().__init__(name, species, age, Characteristic_Feature, Diet)
        self.habitat = habitat
        self.migration_pattern = migration_pattern

    def leave_in_habitat(self):
        print(f"{self.name} has leave in {self.habitat}")

    def can_migrated(self):
        if self.migration_pattern:
            print(f"{self.name} can migrate to other see")
        else:
            print(f"{self.name} can't migrated to other see")
