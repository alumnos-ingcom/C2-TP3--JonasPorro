################
# Jonás Agustín Porro André - @JonasPorro
# TP 4 ejercicio 6
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from Tp4ej1 import ingreso_entero

def ingreso_lista(mensaje, cantidad_elementos):
    lista = [0] * cantidad_elementos
    for i in range(cantidad_elementos):
        lista[i] = ingreso_entero(mensaje)
    return lista

def minimo(lista):
    for i in range(len(lista)):
        if i == 0:
            minimo = lista[i]
        elif minimo > lista[i]:
            minimo = lista[i]
    return minimo

def maximo(lista):
    for i in range(len(lista)):
        if i == 0:
            maximo = lista[i]
        elif maximo < lista[i]:
            maximo = lista[i]
    return maximo

def prueba():
    cantidad_elementos = ingreso_entero("Cuantos elementos va a ingresar a la lista?: ")
    lista = ingreso_lista("Ingrese un numero entero a la lista: ",cantidad_elementos)
    maximo_es = maximo(lista)
    minimo_es = minimo(lista)
    print(f"El máximo elemento de la lista es {maximo_es}, mientras que el minimo es {minimo_es}")

if __name__ == "__main__":
    prueba()