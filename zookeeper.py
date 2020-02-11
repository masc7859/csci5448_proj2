from Subject import Subject
class Zookeeper(Subject):
    state = ""

    def doDuties(self, zooPopulation):
        for animal in zooPopulation:
            self.wakeupAnimal(animal)

        for animal in zooPopulation:
            self.callAnimal(animal)

        for animal in zooPopulation:
            self.feedAnimal(animal)

        for animal in zooPopulation:
            self.exerciseAnimal(animal)

        for animal in zooPopulation:
            self.sleepAnimal(animal)

    def shutdownZoo(self):
        print("Shutting Down Zoo")

    def wakeupAnimal(self, animal):
        print("Waking Up Animal: ")
        animal.wakeup()

    def callAnimal(self, animal):
        print("Calling Animal: ")
        animal.makeNoise()

    def feedAnimal(self, animal):
        print("Feeding Animal: ")
        animal.eat()

    def exerciseAnimal(self, animal):
        print("Exercising Animal: ")
        animal.roam()

    def sleepAnimal(self, animal):
        print("Putting to Sleep Animal: ")
        animal.sleep()
    
    def update(self):
        pass