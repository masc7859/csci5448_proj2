from Subject import Subject
class Zookeeper(Subject):
    state = ""
    observers = []
    def registerobserver(self,observer):
        self.observers.append(observer)
    
    def deregisterobserver(self,observer):
        for i,listedobserver in enumerate(self.observers):
            if(listedobserver == observer):
                del self.observers[i]
                break

    def notifyobservers(self):
        for observer in self.observers:
            observer.update(self.state)

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
        self.state = ""
        print("Shutting Down Zoo")

    def wakeupAnimal(self, animal):
        self.state = "waking"
        self.notifyobservers()
        print("Waking Up Animal: ")
        animal.wakeup()

    def callAnimal(self, animal):
        self.state = "calling"
        self.notifyobservers()
        print("Calling Animal: ")
        animal.makeNoise()

    def feedAnimal(self, animal):
        self.state = "feeding"
        self.notifyobservers()
        print("Feeding Animal: ")
        animal.eat()

    def exerciseAnimal(self, animal):
        self.state = "exercising"
        self.notifyobservers()
        print("Exercising Animal: ")
        animal.roam()

    def sleepAnimal(self, animal):
        self.state = "corraling"
        self.notifyobservers()
        print("Putting to Sleep Animal: ")
        animal.sleep()
    
    def update(self):
        pass