from operaciones import suma, resta, multiplicacion, division

print("Calculadora básica")

while True:
    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))

    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        print("Resultado:", suma(a, b))
    elif opcion == "2":
        print("Resultado:", resta(a, b))
    elif opcion == "3":
        print("Resultado:", multiplicacion(a, b))
    elif opcion == "4":
        print("Resultado:", division(a, b))
    else:
        print("Opción no válida")

    continuar = input("¿Quieres hacer otra operación? (s/n): ").lower()

    if continuar == "n":
        print("Fin del programa.")
        break
    if continuar == "s":
        print("Vuelve a introducir los números")
    else:
        print("Respuesta no válida, escribe 's' o 'n'.")
