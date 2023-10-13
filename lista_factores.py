"""
Diseña un programa para generar la lista de todos los factores de un número entero dado
750722
"""
#Entrada 
numero = int(input("¿De qué número desea los factores?: "))

#Proceso
def obtener_factores(numero):
    factores = []
    for i in range(1, numero + 1):
        if numero % i == 0:
            factores.append(i)
    return factores

if numero <= 0:
    print("Por favor, ingrese un número entero positivo.")
else:
    lista_de_factores = obtener_factores(numero)
    print(f"Los factores de {numero} son: {lista_de_factores}")


