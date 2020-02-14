import sys

class Animal:

    def __init__(self, name, wakeupStrategy):
        self.name = name
        self._wakeupStrategy = wakeupStrategy

    def getName(self):
        return self.name

    #wakeup is delegated to our wakeup strategy for the strategy pattern
    def wakeup(self):
        print(self.name + " the " + self.getAnimalType(), end = ' ')
        self._wakeupStrategy.wakeup()

    def sleep(self):
        print(self.name + " the " + self.getAnimalType() + " goes to sleep.")
