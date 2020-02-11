import abc

class Observer:
    __metaclass__ = abc.ABCMeta
    def update(self,state):
        pass
    