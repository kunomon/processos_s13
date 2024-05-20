from person import Person

# Herança
class Student(Person):
    # constructor
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.__school = school

    def get_info(self):
        return super().get_info() + f' e estuda no {self.__school}'
    
    def change_school(self, newSchool):
        self.__school = newSchool

gabriel = Person('Gabriel', '30')
print(gabriel.get_info())

seiya = Student('Seiya', '16', 'Santuário')
print(seiya.get_info())