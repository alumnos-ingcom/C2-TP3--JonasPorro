################
# Jonás Agustín Porro André - @JonasPorro
# TP 4 ejercicio 11
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def es_palindromo(texto):
    al_reves = texto[::-1]
    if texto == al_reves:
        return True
    else:
        return False

def prueba():
    texto = input("Ingrese una palabra para determinar si es palindromo: ")
    if es_palindromo(texto):
        print(texto + " es palindromo")
    else:
        print(texto + " no es palindromo")

if __name__ == "__main__":
    prueba()