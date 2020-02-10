import abc
from animal import Animal

class WakeupStrategyAbstract(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def wakeup(self):
        print("self.name" + " the " + Animal.getAnimalType() + " wakes up.")

class WakeUpAngryStrategy(WakeupStrategyAbstract):
    def wakeup(self):
        print("wakes up VERY ANGRY.")

class WakeUpNiceStrategy(WakeupStrategyAbstract):
    def wakeup(self):
        print("wakes up really nice.")

class WakeUpReluctantlyStrategy(WakeupStrategyAbstract):
    def wakeup(self):
        print("doesn't really want to wake up...but does anyways.")
