################
# Jonás Agustín Porro André - @JonasPorro
# TP 4 ejercicio 10
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from Tp4ej1 import ingreso_entero
from Tp4ej9 import es_primo

def factores_primos(numero):
    primos = []
    for i in range(2,numero+1):
        while numero % i == 0:
            primos.append(i)
            numero = numero / i
    return tuple(primos)

def prueba():
    numero = ingreso_entero("Ingrese un numero entero positivo para calcular sus factores primos: ")
    if es_primo(numero):
        print(f"{numero} es primo y por lo tanto no se puede descomponer en factores primos.")
    else:
        primos = factores_primos(numero)
        print(f"Los factores primos de {numero} son {primos}")

if __name__ == "__main__":
    prueba()