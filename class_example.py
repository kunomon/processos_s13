# Class Example

class Person:
    # constructor
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def get_info(self):
        return f'{self.__name} tem {self.__age} anos de idade.'
    
gabriel = Person('Gabriel', '30')
print(gabriel.get_info())