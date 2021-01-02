
class Coordenada:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def distancia(self, otra_coordenada):
        x_diff = (self.x - otra_coordenada.x)**2
        y_diff = (self.y - otra_coordenada.y)**2

        return(x_diff +y_diff)**0.5 

class Automovil:

    def __init__(self, modelo, marca, color):
        self.modelo = modelo 
        self.marca = marca
        self.color = color
        self._estado = 'en_reposo'
        self._motor = Motor(cilindros=4) 

    def acelerar(self, tipo='despacio'):

        if tipo == 'rapida':
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)

        self._estado = 'en_movimiento'
    
class Motor:

    def __init__(self, cilindros, tipo = 'gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0

    def inyecta_gasolina(self, cantidad):
        pass

class Lavadora:

    def __init__(self):
        pass

    def lavar(self, temperatura='caliente'):
        self._llenar_tanque_agua(temperatura)
        self._add_soap()
        self._lavar()
        self._centrifugar()

    def _llenar_tanque_agua(self, temperatura):
        print('Llenando el tanque con agua {0}'.format(temperatura))

    def _add_soap(self):
        print('Adding soap')

    def _lavar(self):
        print('Lavando la ropa')

    def _centrifugar(self):
        print('Centrifugando la ropa')

if __name__ == "__main__":
    lavadora = Lavadora()
    lavadora.lavar()
    # coord_1 = Coordenada(3, 30)
    # coord_2 = Coordenada(4, 8) 
    # print(coord_1.distancia(coord_2))
    #print(isinstance(3, Coordenada))
    