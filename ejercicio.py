#!/usr/bin/env python3

cuadrado = lambda x: x**2 

print(cuadrado(6))


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

cuadrados = list(map(lambda x: x**2, numeros))

print(cuadrados)


pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)

from functools import reduce

numero = [1, 2, 3, 4, 5]

producto = reduce(lambda x, y: x*y, numero)

print(producto)
