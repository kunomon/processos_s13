class Professor:
    def __init__(self, nome, cargo, turmas = []):
        self.__nome = nome
        self.__cargo = cargo
        self.__turmas = turmas

    def show_info(self):
        print('Nome do Professor:', self.__nome)
        print('Cargo:', self.__cargo)

        if len(self.__turmas) != 0:
            print('Turmas:')
            for turma in self.__turmas:
                print('  -> ', turma.get_info())