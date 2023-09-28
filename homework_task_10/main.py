
from animals.Mammals.Primates.Gorilla import Gorilla
from animals.Mammals.Primates.Homo_sapiens import Homo_sapiens
from animals.Mammals.Primates.Pan_troglodytes import Pan_troglodytes

from animals.Mammals.Cetaceans.Balaenoptera_musculus import Balaenoptera_musculus
from animals.Mammals.Cetaceans.Delphinidae import Delphinidae
from animals.Mammals.Cetaceans.Orcinus_orca import Orcinus_orca

if __name__ == "__main__":

    Max = Gorilla(

        name="Kin_Kong",
        species="species",
        age=1,
        Characteristic_Feature="Feature",
        Diet="banana",
        tail=True,
        climb_trees=False,
        color="Gray",
        weight_kg=90

    )
    Max.say_hello()
    print('*'*20)
    print(str(Max))
    print('*'*20)
    print(repr(Max))
    print('*'*20)
    Max.has_tail()
    print('*'*20)
    Max.can_climb_tress()
    Max.eat()
    Max.think()
    print('X'*50)

    Alex = Homo_sapiens(

        name="Alex",
        species="species",
        age=2,
        Characteristic_Feature="Feature 2",
        Diet="common food",
        tail=False,
        climb_trees=False,
        color="Gray",
        weight_kg=90

    )

    Alex.say_hello()
    print('*'*20)
    print(str(Alex))
    print('*'*20)
    print(repr(Alex))
    print('*'*20)
    Alex.has_tail()
    print('*'*20)
    Alex.can_climb_tress()
    Alex.eat()
    Alex.think()
    print('*'*20)

    Chita = Pan_troglodytes(

        name="Chita",
        species="species",
        age=3,
        Characteristic_Feature="Feature 3",
        Diet="fruits",
        tail=True,
        climb_trees=True,
        color="Brown",
        weight_kg=10

    )

    Chita.say_hello()
    print('*'*20)
    print(str(Chita))
    print('*'*20)
    print(repr(Chita))
    print('*'*20)
    Chita.has_tail()
    print('*'*20)
    Chita.can_climb_tress()
    Chita.eat()
    Chita.give_birth()
    Chita.think()
    print('*'*20)

    new_musculus = Balaenoptera_musculus (
        name = 'New_musculus',
        species = 'Blue',
        age = 20,
        Characteristic_Feature = "Can eat octopus" ,
        Diet="plankton",
        habitat="Ocean",
        migration_pattern=True,
        vocalizations=True,
        feeding_behavior="Can eat several tons of plancton"
    )
    print(new_musculus.get_description())
    new_musculus.say_hello()
    new_musculus.breach()
    new_musculus.can_migrated()
    new_musculus.find_food()
    new_musculus.interact_with_humans()
    new_musculus.leave_in_habitat()
    new_musculus.eat()
    new_musculus.feature()
    new_musculus.give_birth()
    print('*'*50)

    new_Delphinidae = Delphinidae (
        name = 'New_Delphinidae',
        species = 'Blue',
        age = 15,
        Characteristic_Feature = "Can eat fish" ,
        Diet="fish",
        habitat="sea",
        migration_pattern=True,
        vocalizations=True,
        feeding_behavior="Can eat several kg of fish"
    )
    print(new_Delphinidae.get_description())
    new_Delphinidae.say_hello()
    new_Delphinidae.hunt()
    new_Delphinidae.can_migrated()
    new_Delphinidae.swim()
    new_Delphinidae.jump()
    new_Delphinidae.leave_in_habitat()
    new_Delphinidae.eat()
    new_Delphinidae.feature()
    new_Delphinidae.give_birth()
    new_Delphinidae.play()
    new_Delphinidae.socialize()
    print('*'*100)


    new_Orcinus_orca = Orcinus_orca (
        name = 'New_Orcinus_orca',
        species = 'Black',
        age = 55,
        Characteristic_Feature = "Can eat fish" ,
        Diet="fish",
        habitat="sea and ocean",
        migration_pattern=True,
        vocalizations=False,
        feeding_behavior="Can eat several kg of fish"
    )
    print(new_Orcinus_orca.get_description())
    new_Orcinus_orca.say_hello()
    new_Orcinus_orca.hunt()
    new_Orcinus_orca.can_migrated()
    new_Orcinus_orca.breach()
    new_Orcinus_orca.spy_hop()
    new_Orcinus_orca.leave_in_habitat()
    new_Orcinus_orca.eat()
    new_Orcinus_orca.feature()
    new_Orcinus_orca.give_birth()
    new_Orcinus_orca.hunt()
    new_Orcinus_orca.protect_pod()
    new_Orcinus_orca.interact_with_marine_life()
    print('*'*100)


