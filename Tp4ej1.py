################
# Jonás Agustín Porro André - @JonasPorro
# TP 4 ejercicio 1
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def ingreso_entero(mensaje):
    """
    Esta funcion muestra un mensaje y agrega la # para indicar el ingreso
    de un número entero.
    """
    try:
        entero = int(input(mensaje + " #"))
        return entero
    except ValueError as e:
        print(IngresoIncorrecto("Eso no era un numero!"))
        return None

def ingreso_entero_reintento(mensaje, cantidad_reintentos=5):
    """
    Esta funcion llama a ingreso_entero y si el valor ingresado no es un numero le permite al usuario ingresar uno nuevo.
    El usuario tendrá una cantidad de reintentos determinados por el 2do parámetro (cantidad_reintentos)
    """
    cantidad_intentos = 0
    entero = None
    while entero == None and cantidad_intentos < cantidad_reintentos:
        entero = ingreso_entero(mensaje)
        cantidad_reintentos = cantidad_reintentos - 1
        if entero == None:
            print(F"Le quedan {cantidad_reintentos} intentos.\n")
    if cantidad_intentos == cantidad_reintentos:
        raise NoMasReintentos("Se quedó sin intentos")
    return entero 
    
def ingreso_entero_restringido(mensaje, valor_minimo=0, valor_maximo=10):
    entero = ingreso_entero(mensaje)
    try:
        if entero >= valor_minimo and entero <= valor_maximo:
            return entero
        else:
            raise FueraDeRango("El numero ingresado está fuera del rango determinado.")
            pass
    except TypeError as e:
        raise TypeError("Los valores ingresados no eran numeros") from e

class FueraDeRango(Exception):
    """Esta es la Excepcion para cuando se ingresa un número fuera del rengo establecido"""
    pass

class NoMasReintentos(Exception):
    """Esta es la Excepcion para la falta de reintentos"""
    pass

class IngresoIncorrecto(Exception):
    """Esta es la Excepcion para el ingreso incorrecto"""
    pass

def prueba():
    mensaje = "ingrese un numero"
    valor_minimo = ingreso_entero("Ingrese el límite inferior")
    valor_maximo = ingreso_entero("Ingrese el límite superior")
    entero = ingreso_entero_restringido(mensaje,valor_minimo,valor_maximo)
    #entero = ingreso_entero_reintento(mensaje, 5)
    #entero = ingreso_entero(mensaje)
    print(F"el numero ingresado es {entero}")


if __name__ == "__main__":
    prueba()
    