from animal_classes.canine import Canine

class Wolf(Canine):

    def makeNoise(self):
        print(self.name + " the " + self.getAnimalType() + " makes noise.")

    def getAnimalType(self):
        return self.__class__.__name__
