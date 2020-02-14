from animal import Animal
from zookeeper import Zookeeper
from zooAnnouncer import ZooAnnouncer
import animal_classes
import animals
from wakeup_strategy import WakeUpAngryStrategy
from wakeup_strategy import WakeUpNiceStrategy
from wakeup_strategy import WakeUpReluctantlyStrategy

def populateZoo():
    animalsInZoo = []

    #Instantiate wakeup strategy for the strategy pattern
    angryWakeup = WakeUpAngryStrategy()
    niceWakeup = WakeUpNiceStrategy()
    reluctantWakeup = WakeUpReluctantlyStrategy()

    #Instantiate all animals with the specific wakeup strategy we want them to have
    animalsInZoo.append(animals.cat.Cat("Carl", angryWakeup))
    animalsInZoo.append(animals.dog.Dog("Dan", niceWakeup))
    animalsInZoo.append(animals.elephant.Elephant("Earl", reluctantWakeup))
    animalsInZoo.append(animals.hippo.Hippo("Henry", reluctantWakeup))
    animalsInZoo.append(animals.lion.Lion("Loid", angryWakeup))
    animalsInZoo.append(animals.rhino.Rhino("Rick", niceWakeup))
    animalsInZoo.append(animals.tiger.Tiger("Timmy", reluctantWakeup))
    animalsInZoo.append(animals.wolf.Wolf("Walt", niceWakeup))

    return animalsInZoo

if __name__ == "__main__":
    zooPopulation = populateZoo()

    #Just listing all the animals in the zoo for sanity check
    print("Animals in zoo:")
    for animal in zooPopulation:
        print(animal.getName() + " the " + animal.getAnimalType())

    #Instantiate the announcer for the observer patern
    alex = ZooAnnouncer('Alex')

    zeus = Zookeeper()

    #Make the zookeeper observable by our observer
    zeus.registerobserver(alex)
    zeus.doDuties(zooPopulation)
    zeus.shutdownZoo()
