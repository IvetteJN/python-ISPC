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
# lado1 = input("Ingrese la medida de un lado: ")
# lado2 = input("Ingrese la medida del otro lado: ")
# lado3 = input("Ingrese la medida del tercer lado: ")

# if lado1 == lado2 == lado3:
#     print("El triángulo es equilátero.")
# elif (lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3):
#     print("El triángulo es isósceles.")
# else:
#     print("El triángulo es escaleno.")


# 2. Realice un programa que le permita al usuario simular el pago ingresando el importe y la forma de pago:
# • Contado (1): se aplica un descuento del 10% al importe
# • Tarjeta (2): se aplica un interés de 10%
# • Débito (3): se aplica un descuento del 5%
# Mostrar el importe, el descuento o interés y el importe total.
# importe = float(input("Ingrese el importe: "))
# formaDePago = input("Ingrese el método de pago: \n"
#                     "1.Contado \n"
#                     "2.Tarjeta de crédito \n"
#                     "3.Tarjeta de débito \n")

# if formaDePago == "1":
#     descuento = importe * 0.1
#     print(f'El importe es {importe}')
#     print(f'El descuento es {descuento}')
#     print(f'El total a pagar es {importe - descuento}')
# elif formaDePago == "2":
#     interes = importe * 0.1
#     print(f'El importe es {importe}')
#     print(f'El interés es {interes}')
#     print(f'El total a pagar es {importe + interes}')
# elif formaDePago == "3":
#     descuento = importe * 0.05
#     print(f'El importe es {importe}')
#     print(f'El descuento es {descuento}')
#     print(f'El total a pagar es {importe - descuento}')
# else:
#     print("La forma de pago ingresada no es válida.")

# 3. Realice un programa que lea tres números, muestre cuál es el mayor y determine si es par o impar.
# numero1 = int(input("Ingrese el primer número: "))
# numero2 = int(input("Ingrese el segundo número: "))
# numero3 = int(input("Ingrese el tercer número: "))

# if numero1 > numero2 and numero1 > numero3:
#     print(f"El número {numero1} es mayor que {numero2} y {numero3}")
#     if numero1 % 2 == 0:
#         print("Y es par.")
#     else:
#         print("Y es impar.")
# if numero2 > numero1 and numero2 > numero3:
#     print(f"El número {numero2} es mayor que {numero1} y {numero3}")
#     if numero2 % 2 == 0:
#         print("Y es par.")
#     else:
#         print("Y es impar.")
# if numero3 > numero2 and numero3 > numero1:
#     print(f"El número {numero3} es mayor que {numero2} y {numero1}")
#     if numero3 % 2 == 0:
#         print("Y es par.")
#     else:
#         print("Y es impar.")

# 4. Confeccione un programa que pida un número del 1 al 7 y diga el día de la semana correspondiente.
numero = int(input("Ingrese un número del 1 al 7: "))

if numero == 1:
    print("Es lunes")
elif numero == 2:
    print("Es martes")
elif numero == 3:
    print("Es miércoles")
elif numero == 4:
    print("Es jueves")
elif numero == 5:
    print("Es viernes")
elif numero == 6:
    print("Es sábado")
elif numero == 7:
    print("Es domingo")

# 5. Realice un programa que pida un número del 1 al 12 y diga el nombre del mes correspondiente.
numero = int(input("Ingrese un número del 1 al 12: "))

if numero == 1:
    print("Es enero")
elif numero == 2:
    print("Es febrero")
elif numero == 3:
    print("Es marzo")
elif numero == 4:
    print("Es abril")
elif numero == 5:
    print("Es mayo")
elif numero == 6:
    print("Es junio")
elif numero == 7:
    print("Es julio")
elif numero == 8:
    print("Es agosto")
elif numero == 9:
    print("Es septiembre")
elif numero == 10:
    print("Es octubre")
elif numero == 11:
    print("Es noviembre")
elif numero == 12:
    print("Es diciembre")
