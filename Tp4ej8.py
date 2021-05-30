################
# Jonás Agustín Porro André - @JonasPorro
# TP 4 ejercicio 8
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from Tp4ej1 import ingreso_entero

def ordenar_mayor_a_menor(uno, dos, tres):
    intermedio = None
    tupla = (uno,dos,tres)
    mayor = max(tupla)
    menor = min(tupla)
    dupla = (mayor, menor)
    if uno not in dupla:
        intermedio = uno
    elif dos not in dupla:
        intermedio = dos
    elif tres not in dupla:
        intermedio = tres
    
    if intermedio == None:
        if tupla.count(uno) >= 2:
            intermedio = uno
        elif tupla.count(dos) >= 2:
            intermedio = dos
        elif tupla.count(tres) >= 2:
            intermedio = tres
    
    return(mayor,intermedio,menor)
    
    
def ordenar_menor_a_mayor(uno, dos, tres):
    intermedio = None
    tupla = (uno,dos,tres)
    mayor = max(tupla)
    menor = min(tupla)
    dupla = (mayor, menor)
    if uno not in dupla:
        intermedio = uno
    elif dos not in dupla:
        intermedio = dos
    elif tres not in dupla:
        intermedio = tres
    
    if intermedio == None:
        if tupla.count(uno) >= 2:
            intermedio = uno
        elif tupla.count(dos) >= 2:
            intermedio = dos
        elif tupla.count(tres) >= 2:
            intermedio = tres
    
    return(menor,intermedio,mayor)

def prueba():
    print(f"Ingrese 3 numeros enteros: ")
    uno = ingreso_entero("Ingrese el primer numero: ")
    dos = ingreso_entero("Ingrese el segundo numero: ")
    tres = ingreso_entero("Ingrese el tercer numero: ")
    mayor_a_menor = ordenar_mayor_a_menor(uno,dos,tres)
    menor_a_mayor = ordenar_menor_a_mayor(uno,dos,tres)
    print(f"ordenados de mayor a menor: {mayor_a_menor}")
    print(f"ordenados de menor a mayor: {menor_a_mayor}")    

if __name__ == "__main__":
    prueba()