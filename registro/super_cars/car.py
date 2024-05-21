from engine import Engine

class Car:
    def __init__(self, name, color, year, engine = Engine()):
        self.__name = name
        self.__color = color
        self.__year = year
        self.__engine = engine

    def get_info(self):
        return f'{self.__name} {self.__color} ano {self.__year}, muito top!'
    
    def start(self):
        return f'{self.__engine.start}'
    
# Teste a Classe aqui

# motor_fiasa = Engine('Fiasa')
# uno = Car('Uno', 'azul', '1998')

# vw_apzao = Engine('Volkswage AP')
# verona = Car('Ford Verona', 'vermelho', vw_apzao)

# motor_marea = Engine('Pratola Serra', 'KA-BOOM!')
# marea = Car('Fiat Marea', 'preto', motor_marea)
print(carro.get_info())
print(carro.start())