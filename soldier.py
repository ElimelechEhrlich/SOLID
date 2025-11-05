from abc import ABC, abstractmethod

class Soldier(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def shoot(self):
        pass
    def navigate(self):
        pass
    def callAirSupport(self):
        pass



