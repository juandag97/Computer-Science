import time
import sys
import math 

class Algoritmos():

    def __init__(self, n):
        self.n = n 

    def cte(self):
        return 1

    def lineal(self):
        return self.n 

    def cuadratica(self):
        return (self.n)**2

    def logaritmica(self):
        return math.log10(self.n)

    def lineal_logaritmica(self):
        return self.n * math.log10(self.n)

    def exponencial(self):
        return 2**(self.n)

def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= respuesta 
        n -= 1

    return respuesta 

def factorial_r(n):

    if n == 1:
        return 1
    
    return n * factorial_r(n - 1)

if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    # n = 8000

    # comienzo = time.time()
    #print(factorial(n))
    # factorial(n)
    # final = time.time()
    # print(final - comienzo)

    # comienzo = time.time()
    # #print(factorial_r(n)) 
    # factorial_r(n)
    # final = time.time()
    # print(comienzo, final)
    # print(final - comienzo) 
    algoritmo = Algoritmos(n=10)
    print(algoritmo.lineal()) 
    print(algoritmo.exponencial())
    print(algoritmo.cuadratica())
    print(algoritmo.lineal_logaritmica())   

