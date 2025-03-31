# Programa para ver si es palindromo
def es_palindromo(cadena):
    cadena = cadena.replace(" ", "").lower()
    
    # Verificar si la cadena es igual a su reverso
    if cadena == cadena[::-1]:
        return True
    else:
        return False

entrada = input("Ingresa una palabra para verificar si es palindromo: ")

if es_palindromo(entrada):
    print("Es un palindromo")
else:
    print("No es un palindromo")