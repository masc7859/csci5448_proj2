from Subject import Subject
class Zookeeper(Subject):
    state = ""
    observers = []

    #Makes the zookeeper observable by our observer
    def registerobserver(self,observer):
        self.observers.append(observer)

    #Makes the zookeeper UNobservable by our observer
    def deregisterobserver(self,observer):
        for i,listedobserver in enumerate(self.observers):
            if(listedobserver == observer):
                del self.observers[i]
                break

    #Makes the zookeeper aware of a change in a value
    def notifyobservers(self):
        for observer in self.observers:
            observer.update(self.state)

    #The zookeeper will first wake all animals, then roll call all animals, etc.
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

    #Shuting down zoo in garbage collected and handled language such as python doesn't need to destruct or do much, just stop the obersver from observing
    def shutdownZoo(self):
        self.state = ""
        self.deregisterobserver("Alex")
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

    #This 'state' is simply what the zookeeper is doing at the moment, to be broadcasted to observers
    def setstate(self,state):
        self.state = state
        self.notifyobservers()

    def getstate(self):
        return self.state
