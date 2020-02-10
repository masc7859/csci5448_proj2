
class Animal:

    def __init__(self, name, wakeupStrategy):
        self.name = name
        self._wakeupStrategy = wakeupStrategy

    def getName(self):
        return self.name

    def wakeup(self):
        print(self.name + " the " + self.getAnimalType()),
        self._wakeupStrategy.wakeup()

    def sleep(self):
        print(self.name + " the " + self.getAnimalType() + " goes to sleep.")
