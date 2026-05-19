tareas = []

while True:

    print("\n--- LISTA DE TAREAS ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    # AGREGAR
    if opcion == "1":
        nueva_tarea = input("Ingresa una tarea: ")
        tareas.append(nueva_tarea)
        print("✅ Tarea agregada")

    # MOSTRAR
    elif opcion == "2":

        if len(tareas) == 0:
            print("📭 No hay tareas guardadas")

        else:
            print("\n📋 Tus tareas:")

            for tarea in tareas:
                print("-", tarea)

    # ELIMINAR
    elif opcion == "3":

        if len(tareas) == 0:
            print("❌ No hay tareas para eliminar")

        else:
            print("\n📋 Tareas actuales:")

            for tarea in tareas:
                print("-", tarea)

            eliminar = input("Escribe la tarea a eliminar: ")

            if eliminar in tareas:
                tareas.remove(eliminar)
                print("🗑️ Tarea eliminada")

            else:
                print("⚠️ Esa tarea no existe")

    # SALIR
    elif opcion == "4":
        print("👋 Programa finalizado")
        break

    else:
        print("❌ Opción inválida")