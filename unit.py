from abc import ABC, abstractmethod

# class BirdUnit:
#     def __init__(self):
#         pass
#     def fly(self):
#         return 'We are in the air.!'
    
# class Drone(BirdUnit):
#     pass


# class Tank(BirdUnit):
#     def fly(self):
#         return 'We are not in the air!'

# a = Drone()
# b = Tank()
# print (a.fly())
# print (b.fly())



# זה מפא את העיקרון של ליסקוב מאחר ותת המחלקה 'טנק' משנה ושוברת את ההתנהגות המחלקה הבסיסיתת ואינו רק מרחיב את ההתנהגות - בנוסף למקלחה הראשיתת אלא באה ומפריכה את התכונה.


# הפיתרון:
class Unit(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def operates_on(self):
        pass


class FlyingUnit(Unit):
    def operates_on(self):
        return 'This unit operates on air.'
    
class Drone(FlyingUnit):
    def __init__(self, name):
        super().__init__()
        self.name = name
    def unit_name(self):
        return f'we are {self.name} unit'


class GroundUnit(Unit):
    def operates_on(self):
        return 'This unit operates on the ground.'
    
class Tank(GroundUnit):
    def __init__(self, name):
        super().__init__()
        self.name = name
    def unit_name(self):
        return f'we are {self.name} unit'
    

a = Drone('Drone')
b = Tank('Tank')
print (a.operates_on())
print (a.unit_name())
print (b.operates_on())
print (b.unit_name())