from animals.Mammals.Primates.Primates import Primates


class Pan_troglodytes(Primates):
    def __init__(self, name: str, species: str, age: int, Characteristic_Feature: str, Diet: str, tail: bool, climb_trees: bool, color: str, weight_kg: int) -> None:
        super().__init__(name, species, age, Characteristic_Feature, Diet, tail, climb_trees)
        self.color = color
        self.weight_kg = weight_kg

    def __repr__(self):
        return f"Pan_troglodytes'{self.name}', '{self.species}', {self.age}, '{self.Characteristic_Feature}', '{self.Diet}', {self.tail}, {self.climb_trees}, '{self.color}', {self.weight_kg})"

    def __str__(self):
        return f"Name: {self.name}\nSpecies: {self.species}\nAge: {self.age} years\nCharacteristic Feature: {self.Characteristic_Feature}\nDiet: {self.Diet}\nHas Tail: {'Yes' if self.tail else 'No'}\nClimb Trees: {'Yes' if self.climb_trees else 'No'}\nColor: {self.color}\nWeight: {self.weight_kg} kg"

    def think(self):
        print('I think like a Pan troglodytes')
