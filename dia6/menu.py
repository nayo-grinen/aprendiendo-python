opcion = ""

while opcion != "3":

    print("1. Saludar")
    print("2. Decir adiós")
    print("3. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        print("Hola 👋")

    elif opcion == "2":
        print("Adiós 👋")

    elif opcion == "3":
        print("Programa terminado")