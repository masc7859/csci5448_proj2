import abc
from animal import Animal

#This abstract class is inhereted by our actual strategies for waking up
class WakeupStrategyAbstract(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def wakeup(self):
        print("self.name" + " the " + Animal.getAnimalType() + " wakes up.")

#Our actual alternative methods of waking up for the stragety pattern
class WakeUpAngryStrategy(WakeupStrategyAbstract):
    def wakeup(self):
        print("wakes up VERY ANGRY.")

class WakeUpNiceStrategy(WakeupStrategyAbstract):
    def wakeup(self):
        print("wakes up really nice.")

class WakeUpReluctantlyStrategy(WakeupStrategyAbstract):
    def wakeup(self):
        print("doesn't really want to wake up...but does anyways.")
