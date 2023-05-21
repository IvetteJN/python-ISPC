# Ejercicio estructura condicional simple:
# 1. Realice un programa que solicite dos letras ingresadas por el usuario y verifique si son iguales o no, mostrando un mensaje.
# letra1 = input("Ingrese una letra: ")
# letra2 = input("Ingrese una letra: ")

# if letra1 == letra2:
#     print("Las letras son iguales")
# else:
#     print("Las letras no son iguales")

# 2. Hacer un programa que permita decidir si dos palabras son iguales o diferentes. Mostrar mensaje por pantalla.
# palabra1 = input("Ingrese una palabra: ")
# palabra2 = input("Ingrese una palabra: ")

# if palabra1 == palabra2:
#     print("Las palabras son iguales")
# else:
#     print("Las palabras no son iguales")

# 3. Realizar un programa que permita ingresar “f” o “m” y determinar si vota en mesa femenina o masculina.
# sexo = input("Ingrese F si es femenino o M si es masculino: ")

# if sexo == "F":
#     print("Usted vota en mesa femenina")
# else:
#     print("Usted vota en mesa masculina")

# 4. Realice un programa que lea dos números y diga cuál es el mayor.
# numero1 = input("Ingrese un número: ")
# numero2 = input("Ingrese otro número: ")

# if numero1 > numero2:
#     print(f"El numero {numero1} es mayor que el numero {numero2}")
# else:
#     print(f"El numero {numero2} es mayor que el numero {numero1}")

# 5. Realice un programa que cambie pesos a dólares. Mejórelo, añadiendo el cambio de dólares a pesos y que sea el usuario quién decida qué
# tipo de cambio quiere, si de dólares a pesos o viceversa.
# cambioDeMoneda = int(input("Ingrese el tipo de cambio:\n"
#                            "1.Dolar a Peso\n"
#                            "2.Peso a Dolar\n"))

# if cambioDeMoneda == 1:
#     monto = float(input("Ingrese el monto: "))
#     print(f'{monto} U$D equivalen a {monto*486} Pesos Argentinos')

# elif cambioDeMoneda == 2:
#     monto = float(input("Ingrese el monto: "))
#     print(f'{monto} Pesos Argentinos equivalen a {monto/486} U$D')

# else:
#     print("Ingrese una opcion Valida")

# 6. Realice un programa donde el usuario ingrese su edad. Si es mayor de 16 años, muestre un mensaje diciendo “puede votar”, sino “no vota”.
# edad = input("Ingrese su edad: ")

# if edad > "16":
#     print("Puede votar")
# else:
#     print("No puede votar")

# Ejercicios estructura condicional compuesto (IF anidados)
# 1. Introducir los lados de un triángulo y visualizar por pantalla si dicho triángulo es equilátero, isósceles o escaleno.
lado1 = input("Ingrese la medida de un lado: ")
lado2 = input("Ingrese la medida del otro lado: ")
lado3 = input("Ingrese la medida del tercer lado: ")

if lado1 == lado2 == lado3:
    print("El triángulo es equilátero.")
elif (lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3):
    print("El triángulo es isósceles.")
else:
    print("El triángulo es escaleno.")


# 2. Realice un programa que le permita al usuario simular el pago
# ingresando el importe y la forma de pago:
# • Contado (1): se aplica un descuento del 10% al importe
# • Tarjeta (2): se aplica un interés de 10%
# • Débito (3): se aplica un descuento del 5%
# Mostrar el importe, el descuento o interés y el importe total.
# 3. Realice un programa que lea tres números, muestre cuál es el mayor y
# determine si es par o impar.
# 4. Confeccione un programa que pida un número del 1 al 7 y diga el día de
# la semana correspondiente.
# 5. Realice un programa que pida un número del 1 al 12 y diga el nombre
# del mes correspondiente.
