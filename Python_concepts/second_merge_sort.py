import random 

def merge_sort(lista):
    if len(lista) > 1:
        #Crecimiento logaritmico
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]
        print(izquierda, '*'*5, derecha)

        #Llamada recursiva en cada mitad
        merge_sort(izquierda)
        merge_sort(derecha)
        #Until there
        i, j, k = 0, 0, 0
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1

            k += 1

        # Estos loops copian lo que queda sobrando de la comparacion
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
        print('-'*50)
    return lista 

if __name__ == "__main__":
    list_size = int(input("How length do you want the list to be?"))
    lista = [random.randint(0,100) for i in range(list_size)]
    print(lista)
    print('-'*30)
    print(merge_sort(lista))