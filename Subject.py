import abc

class Subject:
    __metaclass__ = abc.ABCMeta
    def registerobserver(self):
        pass
    
    def deregisterobserver(self):
        pass

    def notifyobservers(self):
        pass