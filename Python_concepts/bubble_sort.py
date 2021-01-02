import random 

def bubble_sort(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista [j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

    return lista

if __name__ == "__main__":
    list_size = int(input('Which is the size of the list? '))
    #target = int(input('Which number you want to find? '))

    lista = [random.randint(0,100) for i in range(list_size)]
    print(lista)
    print(bubble_sort(lista))
    #print(f'El elemento {target} {"esta" if encontrado else "no esta"} en la lista')