#!/usr/bin/env python3

def suma(x, y):
     return x + y

resultado = suma(2, 8)

print(f"\n[+] La suma de ambos valores es {suma(9, 3)}")


variable = "Soy global"

def mi_funcion():
    global variable
    variable = "Soy global y he sido modificado"
    print(variable)

mi_funcion()


print(variable)
