#!/usr/bin/env python3

example = (1, 2, 3, 4, 5)

print(example[:3])

mi_tupla = (1, 2, 3, 4)
a, b, c, d = mi_tupla

print(a)
print(b)
print(c)
print(d)

print(len(mi_tupla))

example2 = (1, "test", (1, 2, 3), 4, True, {'manzanas': 1, 'peras': 5}, 5) # Inmutables insert(), extend(), remove(), append()

mi_tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9)

numeros_pares = tuple(i for i in mi_tupla if i % 2 == 0)

print(numeros_pares)

db1_credential = ("s4vitar", "s4vitar123")
db2_credential = ("hackermate", "hackermate123")

try:
    db1_credential[0] = "manolo"
except TypeError:
    print("No es posible manipular los elementos de una tupla")
