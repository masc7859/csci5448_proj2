from animal_classes.pachyderm import Pachyderm

class Elephant(Pachyderm):

    def makeNoise(self):
        print(self.name + " the " + self.getAnimalType() + " makes noise.")

    def getAnimalType(self):
        return self.__class__.__name__
