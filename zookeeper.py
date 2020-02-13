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
        self.setstate('waking')
        for animal in zooPopulation:
            self.wakeupAnimal(animal)

        self.setstate('calling')    
        for animal in zooPopulation:
            self.callAnimal(animal)

        self.setstate('feeding')
        for animal in zooPopulation:
            self.feedAnimal(animal)

        self.setstate('exercing')
        for animal in zooPopulation:
            self.exerciseAnimal(animal)

        self.setstate('corraling')
        for animal in zooPopulation:
            self.sleepAnimal(animal)

    def shutdownZoo(self):
        self.state = ""
        print("Shutting Down Zoo")

    def wakeupAnimal(self, animal):
        #print("Waking Up Animal: ")
        animal.wakeup()

    def callAnimal(self, animal):
        #print("Calling Animal: ")
        animal.makeNoise()

    def feedAnimal(self, animal):
        #print("Feeding Animal: ")
        animal.eat()

    def exerciseAnimal(self, animal):
        #print("Exercising Animal: ")
        animal.roam()

    def sleepAnimal(self, animal):
        #print("Putting to Sleep Animal: ")
        animal.sleep()
    
    def setstate(self,state):
        self.state = state
        self.notifyobservers()

    def getstate(self):
        return self.state