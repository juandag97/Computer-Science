import random

def busqueda_lineal(lista, objetivo):
    match = False 
    # O(n)
    for elemento in lista:
        if elemento == objetivo:
            match = True
            break
    return match 

if __name__ == "__main__":
    list_size = int(input('Which is the size of the list? '))
    target = int(input('Which number you want to find? '))

    lista = [random.randint(0,100) for i in range(list_size)]
    encontrado = busqueda_lineal(lista, target)
    print(lista)
    print(f'El elemento {target} {"esta" if encontrado else "no esta"} en la lista')