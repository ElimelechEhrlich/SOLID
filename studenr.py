class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

class Calc_grades:
    def __init__(self):
         pass
    @staticmethod
    def calc_average(grades):
            return sum(grades) / len(grades)