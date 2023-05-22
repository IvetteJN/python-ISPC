# Ejercicios estructuras repetitivas y estructuras condicionales.
# 1. Realice un programa que lea 4 números y diga cuántos son pares y cuantos impares y devuelva la sumatoria de los pares.
# sum = 0

# par = 0
# impar = 0
# for i in range(4):
#     numero = int(input("Ingrese un numero: "))
#     if numero % 2 == 0:
#         print(f"{numero} es par")
#         sum += numero
#         par += 1
#     else:
#         print(f"{numero} es impar")
#         impar += 1

# print(f"La suma total de numeros pares es: {sum}")
# print(f"La cantidad de numeros pares es: {par} y de impares es: {impar}")

# 2. Leer 10 números y obtener la cantidad de mayores y la cantidad de menores a 100, cuál es el número máximo y cuál es el número mínimo.
# maximo = minimo = mayor = menor = 0

# for i in range(10):
#     numero = int(input("Ingrese un número: "))
#     if i == 0:
#         maximo = numero
#     elif numero > maximo:
#         maximo = numero
#     if i == 0:
#         minimo = numero
#     elif numero < minimo:
#         minimo = numero
#     if numero > 100:
#         mayor += 1
#     else:
#         menor += 1

# print(f"La cantidad de numeros mayores a 100 es: {mayor}")
# print(f"La cantidad de numeros menores a 100 es: {menor}")
# print(f"El mayor es: {maximo}")
# print(f"El menor es: {minimo}")

# 3. Ingresar las edades y el sexo de 15 personas y determinar cuántas son mujeres, cuántos varones, cuántos mayores de edad y cuántos
# menores de edad.
# edad = genero = masculino = femenino = mayor = menor = 0

# for i in range(15):
#     edad = int(input("Ingrese su edad: "))
#     genero = input("Ingrese su genero (F) femenino o (M) masculino: ").lower()
#     if genero == "f":
#         femenino += 1
#     else:
#         masculino += 1
#     if edad > 18:
#         mayor += 1
#     else:
#         menor += 1

# print(f"La cantidad de hombres es de: {masculino} personas")
# print(f"La cantidad de mujeres es de: {femenino} personas")
# print(f"Hay {mayor} mayores de edad")
# print(f"Hay {menor} menores de edad")

# 4. Leer 10 números y mostrar solamente los números positivos, y su sumatoria.
# positivo = []
# sumatoria = 0

# for i in range(10):
#     numero = int(input("Ingrese un número: "))
#     if numero > 0:
#         positivo.append(numero)
#         sumatoria += numero

# print(f"Los numeros positivos son: {positivo}")
# print(f"La suma de los numeros positivos es: {sumatoria}")

# 5. Leer 15 números negativos y convertirlos a positivos e imprimir dichos números.
positivos = 0
for i in range(15):
    numero = int(input("Ingrese números negativos: "))
    positivos = numero*(-1)
    print(f"Numero: {positivos}")
