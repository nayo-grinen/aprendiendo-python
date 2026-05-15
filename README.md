# Aprendiendo Python 🚀

Mi camino aprendiendo programación desde cero.

---

## Día 1 — Comenzamos tu camino en programación 🚀
1. Objetivo de hoy

preparar tu entorno de trabajo
entender qué es programar
instalar Python y VS Code
escribir tu primer programa
crear tu cuenta/proyecto en GitHub

¿Qué es programar?

Programar es darle instrucciones a una computadora paso a paso.

Un programa es simplemente:

entrada -> procesamiento -> resultado

Ejemplo:

nombre = "Ana"
print("Hola", nombre)

La computadora:

guarda un dato
procesa la instrucción
muestra un resultado

Instala:
Python

Descargar desde:
Python
VS Code
Git

Meta final del día

Hoy deberías terminar con:
✅ Python instalado
✅ VS Code instalado
✅ Git instalado
✅ Tu primer programa funcionando
✅ Cuenta GitHub creada
✅ Primer repositorio
✅ Primer commit

---

## Día 2 — Variables y primeros programas interactivos 💻
1. Objetivo de hoy

Hoy aprenderás:

qué son las variables
tipos básicos de datos
cómo recibir información del usuario
cómo combinar texto y datos
cómo guardar avances en GitHub

¿Qué es una variable?

Una variable es una “caja” donde guardamos información.

Ejemplo:

nombre = "Carlos"
edad = 25

Aquí:

nombre guarda texto
edad guarda números
Tipos de datos básicos
Texto → string
ciudad = "Santiago"
Número entero → int
edad = 20
Decimal → float
altura = 1.75
Verdadero/Falso → boolean
estudia = True
3. input() — interacción con usuarios
Programa básico
nombre = input("¿Cómo te llamas? ")

print("Hola")
print(nombre)

La computadora:

pregunta
espera respuesta
muestra resultado

Meta final del día

Hoy deberías terminar con:
✅ programas interactivos
✅ uso de variables
✅ manejo de input()
✅ mini proyecto funcional
✅ README actualizado
✅ nuevo commit en GitHub

Archivos creados:
- usuario.py
- ciudad_favorita.py
- perfil.py
- meta.py

---

## Día 3 — Operaciones matemáticas y calculadoras 🧮
1. Objetivo de hoy

operaciones matemáticas en Python
conversión de datos (int() y float())
cómo hacer cálculos con información del usuario
lógica básica de programas
cómo estructurar mejor tus proyectos

Operadores matemáticos
Suma
print(5 + 3)
Resta
print(10 - 4)
Multiplicación
print(6 * 2)
División
print(20 / 5)
3. El problema importante: input() devuelve texto

Mira esto:

numero = input("Ingresa un número: ")

Aunque escribas:

5

Python lo guarda como texto.

Por eso necesitamos convertir.

4. Conversión de tipos
int()

Convierte a entero:

edad = int(input("Edad: "))
float()

Convierte a decimal:

altura = float(input("Altura: "))
5. Primer programa matemático
Archivo:
suma.py

Código:

numero1 = int(input("Primer número: "))
numero2 = int(input("Segundo número: "))

resultado = numero1 + numero2

print("Resultado:")
print(resultado)

Extra práctica mental 🧠

Antes de escribir código, piensa:

Entrada

¿Qué datos necesita el programa?

Proceso

¿Qué cálculo hará?

Salida

¿Qué mostrará?

Eso es la base de casi toda la programación.

Meta final del día

Hoy deberías terminar con:
✅ operaciones matemáticas
✅ conversión de tipos
✅ programas con cálculos
✅ calculadora funcional
✅ README actualizado
✅ nuevo commit en GitHub

Aprendí:
- Operaciones matemáticas
- int() y float()
- Calculadoras simples
- Entrada → proceso → salida

# DÍA 4 — Condicionales (if) y toma de decisiones 🧠
1. Objetivo de hoy

cómo hacer que un programa tome decisiones
usar if, elif y else
comparaciones básicas
lógica de programación real
crear programas más inteligentes

¿Qué es un condicional?

Permite que el programa decida qué hacer según una condición.

Ejemplo:

edad = 18

if edad >= 18:
    print("Eres mayor de edad")
3. Operadores de comparación
Igual
==
Distinto
!=
Mayor que
>
Menor que
<
Mayor o igual
>=
Menor o igual
<=
4. Primer programa con decisiones
Archivo:
edad.py

Código:

edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Puedes entrar")
5. else

Sirve para ejecutar otra acción si NO se cumple la condición.

edad = int(input("Edad: "))

if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")
6. elif

Permite agregar más opciones.

nota = float(input("Nota: "))

if nota >= 6:
    print("Excelente")
elif nota >= 4:
    print("Aprobado")
else:
    print("Reprobado")

Meta final del día

Hoy deberías terminar con:
✅ uso de if
✅ programas con decisiones
✅ comparaciones
✅ mini proyecto funcional
✅ README actualizado
✅ nuevo commit en GitHub

Aprendí:
- if
- elif
- else
- comparaciones
- lógica básica

# DÍA 5 — Operadores lógicos 🔥
1. Objetivo

combinar condiciones
crear validaciones más inteligentes
usar:
and
or
not

Esto hace que tus programas se parezcan más a aplicaciones reales.

2. Teoría
AND

Significa:
👉 ambas condiciones deben cumplirse.

Ejemplo:

edad = 20
tiene_entrada = True

if edad >= 18 and tiene_entrada == True:
    print("Puede entrar")

Aquí:

debe ser mayor de edad
Y tener entrada

Las dos.

3. OR

Significa:
👉 al menos una condición debe cumplirse.

dia = "sabado"

if dia == "sabado" or dia == "domingo":
    print("Es fin de semana")
4. NOT

Invierte el valor.

llueve = False

if not llueve:
    print("Podemos salir")
5. Ejercicios prácticos
Ejercicio 1 — Acceso
edad = int(input("Edad: "))
entrada = input("¿Tienes entrada? ")

if edad >= 18 and entrada == "si":
    print("Acceso permitido")
else:
    print("No puedes entrar")
Ejercicio 2 — Descuento
edad = int(input("Edad: "))

if edad < 12 or edad > 60:
    print("Tienes descuento")
else:
    print("No tienes descuento")
6. Mini proyecto 🔥
Proyecto: “Sistema de login simple”

Archivo:

login.py

Objetivo:

pedir usuario
pedir contraseña
validar acceso

Ejemplo:

usuario = input("Usuario: ")
clave = input("Contraseña: ")

if usuario == "admin" and clave == "python123":
    print("Bienvenida")
else:
    print("Datos incorrectos")
7. Extra challenge ⚡

Agregar:

intentos incorrectos
mensaje personalizado
emojis
validación de mayúsculas

Aprendí:
- and
- or
- not
- validaciones
- lógica más avanzada

# DÍA 6 — Bucles (for y while) 🔁
1. Objetivo

repetir acciones automáticamente
evitar escribir código muchas veces
usar:
for
while
crear programas repetitivos e interactivos

Esto es una de las bases MÁS importantes de programación.

2. ¿Qué es un loop?

Un loop repite instrucciones.

En vez de:

print("Hola")
print("Hola")
print("Hola")

Haces:

for i in range(3):
    print("Hola")

Mucho más elegante 😌

3. FOR

Se usa cuando sabes cuántas veces repetir algo.

Ejemplo
for i in range(5):
    print("Python")

Resultado:

Python
Python
Python
Python
Python
4. range()
range(5)

Va desde:

0 → 4

Porque Python empieza en 0.
Eso al principio le vuela la cabeza a todo el mundo un poquito. Tradición ancestral del caos tecnológico.

5. Mostrar números
for i in range(5):
    print(i)

Resultado:

0
1
2
3
4
6. WHILE

Repite mientras una condición sea verdadera.

contador = 0

while contador < 5:
    print(contador)
    contador = contador + 1

MUY importante:

contador = contador + 1

Porque si no:
☠️ loop infinito ☠️

Y el computador entra en modo “he decidido vivir aquí para siempre”.

7. Ejercicios prácticos
Ejercicio 1 — Contar del 1 al 10
for i in range(1, 11):
    print(i)
Ejercicio 2 — Tabla del 5
for i in range(1, 11):
    print(5 * i)
Ejercicio 3 — Password infinita
clave = ""

while clave != "python":
    clave = input("Ingresa la clave: ")

print("Acceso permitido")
8. Mini proyecto 🔥
Proyecto: “Mini menú interactivo”

Archivo:

menu.py

Objetivo:
Mostrar opciones hasta que el usuario quiera salir.

Ejemplo:

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
9. Lo importante de hoy 🧠

Aquí empieza a aparecer algo MUY real de programación:

Automatización

Los loops permiten:

repetir tareas
recorrer datos
crear menús
juegos
sistemas
bots
automatizaciones

Son gigantescos.

