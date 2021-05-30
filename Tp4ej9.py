################
# Jonás Agustín Porro André - @JonasPorro
# TP 4 ejercicio 9
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from Tp4ej1 import ingreso_entero

def es_primo(numero):
    for i in range(numero):
        if i+1 == numero:
            return True
        if i+1 == 1:
            pass
        else:
            resto = numero % (i+1)
            if resto == 0:
                return False
    
def prueba():
    numero = ingreso_entero("Ingrese un numero entero para determinar si es o no primo: ")
    if numero == 1 or numero == 0:
        print("Los numeros 1 y 0 no son primos ni compuestos.")
    elif numero < 0:
        print("Los numeros negativos no son primos.")
    elif es_primo(numero):
        print(f"{numero} es primo.")
    else:
        print(f"{numero} no es primo.")

if __name__ == "__main__":
    prueba()