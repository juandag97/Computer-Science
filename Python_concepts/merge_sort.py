import random 

def merge_sort(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]
        print(izquierda, '*'*5, derecha)

        #Llamada recursiva en cada mitad
        merge_sort(izquierda)
        merge_sort(derecha)

        #Iteradores para recorrer las dos sublistas
        i, j, k = 0, 0, 0
        #iterador lista principal K
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1
        print(f'Izquierda {izquierda}, derecha {derecha}')
        print(lista)
        print('-' * 50)

        return lista

if __name__ == "__main__":
    list_size = int(input('Which is the size of the list? '))
    #target = int(input('Which number you want to find? '))

    lista = [random.randint(0,100) for i in range(list_size)]
    print(lista)
    print('-'*20)
    print(merge_sort(lista))
