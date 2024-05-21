class Aluno:
    def __init__(self, nome, turmas):
        self.__nome = nome
        self.__turmas = turmas

    def show_info(self):
        print('Nome do Aluno: ', self.__nome)
        print('Turmas: ')

        for turma in self.__turmas:
            print('  -> ', turma.get_info())