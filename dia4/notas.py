nombre = input("Nombre: ")
nota = float(input("Nota: "))

print("----- RESULTADO -----")

if nota >= 6:
    print(nombre, "tiene un desempeño excelente")
elif nota >= 4:
    print(nombre, "aprobó")
else:
    print(nombre, "reprobó")