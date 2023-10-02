from CustomIterator import CustomIterator


class Carriage():
    def __init__(self, number: int) -> None:
        self.number = number
        self.passengers = []

    def add_passengers(self, passenger_name: str):
        if len(self.passengers) < 10:
            self.passengers.append(passenger_name)
        else:
            raise ValueError(f"Вагон {self.number} заповнений. Неможливо додати більше пасажирів.")

    def __len__(self):
        return len(self.passengers)

    def __iter__(self):
        return CustomIterator(self.passengers, 0, len(self.passengers))

    def __str__(self):
        if len(self.passengers) == 0:
            passengers_info = [
                f"Номер вагона:[{self.number}]; Вагон наразі пустий"]
        else:
            passengers_info = [
                f"Номер вагона:[{self.number}]; Им'я пасажира: {name}" for name in self.passengers]
        return "\n".join(passengers_info)
