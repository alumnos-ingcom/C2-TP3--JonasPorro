################
# Jonás Agustín Porro André - @JonasPorro
# TP 4 ejercicio 7
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from Tp4ej1 import ingreso_entero

def division_lenta(dividendo, divisor):
    if divisor == 0:
        raise DivisionPorCero("No se puede dividir por cero!")
    resto = dividendo
    cociente = 0
    while resto >= divisor:
        resto = resto - divisor
        cociente = cociente +1
    return (cociente,resto)

class DivisionPorCero(Exception):
    """
    Excepción para cuando se intenta dividir por cero.
    """
    pass

def prueba():
    dividendo = ingreso_entero("Ingrese un dividendo entero: ")
    divisor = ingreso_entero("Ingrese un divisor entero: ")
    (cociente,resto) = division_lenta(dividendo,divisor)
    print(f"La division entre {dividendo} y {divisor} da {cociente} como cociente y {resto} como resto.")

if __name__ == "__main__":
    prueba()