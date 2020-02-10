from animal import Animal

class Feline(Animal):

    def roam(self):
        print(self.name + " the " + self.getAnimalType() + " roams around.")

    def eat(self):
        print(self.name + " the " + self.getAnimalType() + " eats.")
