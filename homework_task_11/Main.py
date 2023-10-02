
from Carriage import Carriage
from Train import Train

if __name__ == '__main__':
    wagon1 = Carriage(1)
    wagon2 = Carriage(2)
    wagon3 = Carriage(3)
    Train1 = Train("KN 1242", "Sumy -> Odesa")
    Train1.add_cariage(wagon1)
    Train1.add_cariage(wagon2)
    Train1.add_cariage(wagon3)
    wagon1.add_passengers("Mark")
    wagon1.add_passengers("Alex")
    wagon1.add_passengers("Micle")
    wagon1.add_passengers("Vita")
    wagon1.add_passengers("Vita")
    wagon1.add_passengers("Vita")
    wagon1.add_passengers("Vita")
    wagon1.add_passengers("Vita")
    wagon1.add_passengers("Vita")
    wagon1.add_passengers("Vita")
    print(Train1.info())
    print(Train1)
    print(wagon3)
    print(len(Train1))
    print(len(wagon1))
    print(wagon1)
    print(wagon2)
