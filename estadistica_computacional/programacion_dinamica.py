import sys

def fibonacci_recursivo(n):

    if n == 0 or n == 1:
        return 1

    return fibonacci_recursivo(n-1) + fibonacci_recursivo(n - 2)

def fibonnaci_dinamico(n, memo = {}):

    if n == 0 or n == 1:
        return 1

    try:
        return memo[n]
    except KeyError:
        resultado = fibonnaci_dinamico(n-1, memo) + fibonnaci_dinamico(n - 2, memo)
        memo[n] = resultado

        return resultado


if __name__ == "__main__":
    sys.setrecursionlimit(100002)
    n = int(input('Escoge un numero: '))
    print(fibonnaci_dinamico(n))
    