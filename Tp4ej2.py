################
# Jonás Agustín Porro André - @JonasPorro
# TP 4 ejercicio 2
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from Tp4ej1 import ingreso_entero

def suma_lenta(numero, otro_numero):
    try:
        if (numero < 0 and otro_numero >= 0) or (numero >= 0 and otro_numero >= 0):
            for i in range(otro_numero):
                numero = numero + 1
            return numero
                
        elif numero >= 0 and otro_numero < 0:
            for i in range(numero):
                otro_numero = otro_numero + 1
            return otro_numero
                
        elif numero < 0 and otro_numero < 0:
            for i in range(-otro_numero):
                numero = numero - 1
            return numero
                
    except TypeError as e:
        raise TypeError("Los valores ingresados no eran numeros") from e


def prueba():
    numero_a = ingreso_entero("ingrese el primer numero a sumar")
    numero_b = ingreso_entero("ingrese el segundo numero a sumar")
    resultado = suma_lenta(numero_a,numero_b)
    print(f"El resultado de la suma es {resultado}")
    pass

if __name__ == "__main__":
    prueba()