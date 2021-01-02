import random 

def busqueda_binaria(lista, comienzo, final, objetivo):
    print(f'Buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')
    if comienzo > final:
        return False
    #// Division de enteros
    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        return True
    #El +1 y -1 en los elif se genera por el indice 0
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo)
    elif lista[medio] > objetivo:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo)

if __name__ == "__main__":
    list_size = int(input('Which is the size of the list? '))
    target = int(input('Which number you want to find? '))

    lista = sorted([random.randint(0,100) for i in range(list_size)])
    encontrado = busqueda_binaria(lista, 0, len(lista), target)
    print(lista)
    print(f'El elemento {target} {"esta" if encontrado else "no esta"} en la lista')