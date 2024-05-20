class Student:
    # constructor
    def __init__(self, name, age, school):
        self.__name = name
        self.__age = age
        self.__school = school

    def get_info(self):
        return f'{self.__name} tem {self.__age} anos de idade e estuda no {self.__school}'