edad = int(input("Edad: "))
entrada = input("¿Tienes entrada? ")

if edad >= 18 and entrada == "si":
    print("Acceso permitido")
else:
    print("No puedes entrar")