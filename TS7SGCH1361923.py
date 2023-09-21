"""Supervisado de programacion 
21/09/2023
Stefanny Gisselle Carpio Hidalgo"""

nombre_completo = print("Gisselle Carpio")

while True:
    try:
        numero = int(input("Ingrese un número del 1 al 10 (o escriba SALIR para salir): "))
        
        if numero < 1 or numero > 10:
            print("El número debe estar en el rango de 1 a 10.")
            continue
        
        for i in range(1, 11):
            resultado = numero * i
            print(f"{numero} X {i} = {resultado}")
        
        opcion = input("¿Desea generar la tabla de otro número? (SALIR para salir): ").upper()
        if opcion == "SALIR":
            break
    except ValueError:
        print("Por favor, ingrese un número válido.")
