from animal_classes.pachyderm import Pachyderm
import random

class Hippo(Pachyderm):

    #This is our random action implementation. Instead of making noise the animal may do something else
    def makeNoise(self):
        randAction = random.randint(0,100)
        if(randAction < 25):
            print(self.name + " the " + self.getAnimalType() + " makes noise.")
        elif(randAction < 50):
            self.eat()
        elif(randAction < 75):
            self.roam()
        else:
            self.sleep()

    def getAnimalType(self):
        return self.__class__.__name__
