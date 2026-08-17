from time import perf_counter
from AP_03_ordenacao import divide_and_conquer_sort, quick_sort, selection_sort
from random import randint, seed
from sys import setrecursionlimit as lim

lim(100000) #deixar que a recursao continue
seed(1001) #quebrar aleatoriedade do algoritmo para que fique tudo igual ao gabarito

def lista_random(n):
    return [randint(0, n) for i in range(0, n)]

def lista_pior(n):
    return [i for i in range(n, 0, -1)]

def benchmark(k, *n):
    texto = ""
    for i in range(2):
        for j in range(3):
            for l in n:
                if j == 0:
                    texto += f"| Merge sort    "
                elif j == 1:
                    texto += f"| Quick sort    "
                else:
                    texto += f"| Selection sort"
                texto += f"| Caso medio " if i == 0 else f"| Pior caso  "
                soma = 0
                for __ in range(k):
                    lista_teste = []
                    if i == 0:
                        lista_teste = lista_random(l)
                    else:
                        lista_teste = lista_pior(l)
                    if j == 0:
                        soma -= perf_counter()
                        divide_and_conquer_sort(lista_teste)
                        soma += perf_counter()
                    elif j == 1:
                        soma -= perf_counter()
                        quick_sort(lista_teste)
                        soma += perf_counter()
                    else:
                        soma -= perf_counter()
                        selection_sort(lista_teste)
                        soma += perf_counter()
                texto += f"| N: {l:>6}    | Tempo medio: {soma / k}\n"
    return texto 

print(benchmark(50, 100, 500, 1000, 5000))