from student import Student

saintSeiyaAge = 16
saintSeiyaSchool = 'Santuário'
# Lista de Students
students = [
    Student('Seiya', saintSeiyaAge, saintSeiyaSchool),
    Student('Shiryū', saintSeiyaAge, saintSeiyaSchool),
    Student('Hyoga', saintSeiyaAge, saintSeiyaSchool),
    Student('Shun', saintSeiyaAge, saintSeiyaSchool),
    Student('Ikki', 18, saintSeiyaSchool),
]

class StudentList:
    # constructor
    def __init__(self):
        self.__list = students

    def get(self):
        return self.__list
    
    def print_info(self):
        for student in self.__list:
            print(student.get_info())

listaAlunos = StudentList()
listaAlunos.print_info()