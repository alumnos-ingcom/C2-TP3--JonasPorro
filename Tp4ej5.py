################
# Jonás Agustín Porro André - @JonasPorro
# TP 4 ejercicio 5
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from Tp4ej1 import ingreso_entero

def signo(numero):
    if numero < 0:
        return -1
    elif numero == 0:
        return 0
    else:
        return 1

def prueba():
    numero = ingreso_entero("Ingrese un numero entero: ")
    signo_resultado = signo(numero)
    if signo_resultado == -1:
        print(f"{numero} es negativo")
    elif signo_resultado == 0:
        print("El valor ingresado es 0")
    elif signo_resultado == 1:
        print(f"{numero} es positivo")

if __name__ == "__main__":
    prueba()