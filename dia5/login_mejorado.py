usuario_correcto = "admin"
contrasena_correcta = "python123"

intentos = 0

while intentos < 3:

    usuario = input("👤 Usuario: ").lower()
    contrasena = input("🔒 Contraseña: ")

    if usuario == usuario_correcto and contrasena == contrasena_correcta:
        print("✅ Bienvenida", usuario)
        break

    else:
        intentos = intentos + 1
        print("❌ Datos incorrectos")
        print("⚠️ Intento número:", intentos)

if intentos == 3:
    print("🚫 Cuenta bloqueada")