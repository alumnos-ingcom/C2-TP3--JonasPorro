################
# Jonás Agustín Porro André - @JonasPorro
# TP 4 ejercicio 3
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from Tp4ej1 import ingreso_entero
from Tp4ej1 import IngresoIncorrecto

def ingreso_real(mensaje):
    """
    Esta funcion muestra un mensaje y agrega la # para indicar el ingreso
    de un número real.
    """
    try:
        real = float(input(mensaje + " #"))
        return real
    except ValueError as e:
        print(IngresoIncorrecto("Eso no era un numero!"))
        return None

def convertir_a_fahrenheit(centigrados):
    fahrenheit = (centigrados * 9/5) + 32
    return fahrenheit
    
def convertir_a_centigrados(fahrenheit):
    centigrados = (fahrenheit - 32) * 5/9
    return centigrados

def prueba():
    print("Escoja una opción:\n1 - Centigrados a Fahrenheit \n2 - Fahrenheit a Centigrados")
    eleccion = ingreso_entero("Elección: ")
    if eleccion == 1:
        print("\nHa escogido convertir de Centigrados a Fahrenheit.")
        centigrados = ingreso_real("Ingrese el valor a convertir: ")
        fahrenheit = convertir_a_fahrenheit(centigrados)
        print(f"{centigrados} ºC equivalen a {fahrenheit} ºF")
    elif eleccion == 2:
        print("\nHa escogido convertir de Fahrenheit a Centigrados.")
        fahrenheit = ingreso_real("Ingrese el valor a convertir: ")
        centigrados = convertir_a_centigrados(fahrenheit)
        print(f"{fahrenheit} ºF equivalen a {centigrados} ºC")
    else:
        print("Opción incorrecta.")

if __name__ == "__main__":
    prueba()