from animal import Animal
from zookeeper import Zookeeper
from zooAnnouncer import ZooAnnouncer
import animal_classes
import animals

def populateZoo():
    animalsInZoo = []
    animalsInZoo.append(animals.cat.Cat("Carl"))
    animalsInZoo.append(animals.dog.Dog("Dan"))
    animalsInZoo.append(animals.elephant.Elephant("Earl"))
    animalsInZoo.append(animals.hippo.Hippo("Henry"))
    animalsInZoo.append(animals.lion.Lion("Loid"))
    animalsInZoo.append(animals.rhino.Rhino("Rick"))
    animalsInZoo.append(animals.tiger.Tiger("Timmy"))
    animalsInZoo.append(animals.wolf.Wolf("Walt"))

    return animalsInZoo

if __name__ == "__main__":
    zooPopulation = populateZoo()
    print("Animals in zoo:")
    for animal in zooPopulation:
        print(animal.getName() + " the " + animal.getAnimalType())
    alex = ZooAnnouncer('Alex')
    zeus = Zookeeper()

    zeus.registerobserver(alex)
    zeus.doDuties(zooPopulation)
    zeus.shutdownZoo()
