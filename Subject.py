from abc import ABC, abstractmethod 
class Subject(ABC):
    def registerobserver(self):
        pass
    
    def deregisterobserver(self):
        pass

    def notifyobservers(self):
        pass