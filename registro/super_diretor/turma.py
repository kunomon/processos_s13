class Turma:
    def __init__(self, nome, ano):
        self.__nome = nome
        self.__ano = ano

    def get_info(self):
        return f'{self.__nome} - {self.__ano}'