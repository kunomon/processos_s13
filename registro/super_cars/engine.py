class Engine:
    def __init__(self, name, motorSound = 'Vrum vrum!'):
        self.__name = name
        self.__sound = motorSound

    def get_name(self):
        return self.__name

    def start(self):
        return self.__sound