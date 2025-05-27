#!/usr/bin/env python3

first_number = 12
second_number = 7

result = first_number ** second_number

print("{:,}".format(result).replace(",", "."))

first_str = "Hola"
second_str = " "
third_str = "mundo"

print(third_str[0:3]*5)

odd_numbers = [1,3,5,7,9]
even_numbers = [2,4,6,8]

result = list(map(sum, zip(odd_numbers, even_numbers)))

print(result)

name = "guille"
rol = "lammer"
edad = 23

print("Hola, mi nombre es %s y soy un %s. Actualmente tengo %d" % (name, rol, edad))

print("Hola, soy {}!".format(name))
print("Hola soy {0}! y tengo {1}. No es broma, mi nombre real es {0}". format(name, edad))
