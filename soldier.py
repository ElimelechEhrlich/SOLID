from abc import ABC, abstractmethod

class Shooter(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def shoot(self):
        return 'shoot.'

class Navigator(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def navigate(self):
        return 'navigate.'

class AirSupportCaller(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def callAirSupport(self):
        return 'call Air Support.'



class Infantry(Shooter, Navigator):
    def __init__(self, unit_name):
        super().__init__(self)
        self.unit_name = unit_name

class ForwardObserver(Shooter, AirSupportCaller):
    def __init__(self, unit_name):
        super().__init__(self)
        self.unit_name = unit_name

class Pilot(AirSupportCaller):
    def __init__(self, unit_name):
        super().__init__(self)
        self.unit_name = unit_name



a = Infantry('aaa')
print (a.shoot())
print (a.navigate())
b = ForwardObserver('bbb')
print (b.shoot())
print (b.callAirSupport())
c = Pilot('ccc')
print (c.callAirSupport())


