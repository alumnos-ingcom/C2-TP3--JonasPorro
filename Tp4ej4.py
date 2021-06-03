################
# Jonás Agustín Porro André - @JonasPorro
# TP 4 ejercicio 4
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from Tp4ej1 import ingreso_entero

def compara(numero, otro_numero):
    if numero < otro_numero:
        return -1
    elif numero == otro_numero:
        return 0
    else:
        return 1
    
def prueba():
    print("Se compararán dos numeros enteros: ")
    numero_a = ingreso_entero("Ingrese el primer valor: ")
    numero_b = ingreso_entero("Ingrese el segundo valor: ")
    comparacion = compara(numero_a,numero_b)
    if comparacion == -1:
        print(f"{numero_a} es menor que {numero_b}")
    elif comparacion == 0:
        print("Los valores ingresados son iguales")
    elif comparacion == 1:
        print(f"{numero_a} es mayor que {numero_b}")
        
if __name__ == "__main__":
    prueba()