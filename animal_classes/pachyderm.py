from animal import Animal

class Pachyderm(Animal):

    def roam(self):
        print(self.name + " the " + self.getAnimalType() + " roams around.")

    def eat(self):
        print(self.name + " the " + self.getAnimalType() + " eats.")
