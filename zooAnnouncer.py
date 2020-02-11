from Observer import Observer
class ZooAnnouncer(Observer):
    name = ""
    def __init__(self,name):
        self.name = name
    def update(self,state):
        print(self.name + " reporting, the zookeeper is " + state + " the animals")