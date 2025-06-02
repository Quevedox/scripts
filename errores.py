#!/usr/bin/env python3

from pwn import log

try:
    num = "hola"/0

except ZeroDivisionError:
    print("No se puede dividir un numero entre cero")

except TypeError:
    log.failure("Las operatorias matematicas solo deben realizarse con numeros!")

else:
    print(f"La division de ambos numeros da como resultado {num}")

finally:
    print("Esto siempre se va a ejecutar")



