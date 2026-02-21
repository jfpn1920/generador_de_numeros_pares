inicio = int(input("Ingrese el número inicial del rango: "))
fin = int(input("Ingrese el número final del rango: "))
print("\nNúmeros pares en el rango:")
for numero in range(inicio, fin + 1):
    if numero % 2 == 0:
        print(numero)