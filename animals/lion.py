from animal_classes.feline import Feline

class Lion(Feline):

    def makeNoise(self):
        print(self.name + " the " + self.getAnimalType() + " makes noise.")

    def getAnimalType(self):
        return self.__class__.__name__
