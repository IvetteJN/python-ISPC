# 1) Escribir un programa que permita validar el ingreso a un sistema. Se deberá solicitar el ingreso por teclado de nombre de usuario
# y contraseña. Será valido como nombre de usuario “admin” y como contraseña “1234”. Si el ingreso es correcto deberá mostrar por pantalla
# el mensaje “Ingreso exitoso”.
# Opcional 1: permitir como usuario valido también su propio nombre y su propia contraseña.
# Opcional 2: solamente permitir el ingreso incorrecto de los datos 3 veces, luego de ello, no permitir más ingresos y mostrar por
# pantalla “Cuenta bloqueada”.

# 2) Mostrar por pantalla el siguiente menú:
# CAJERO AUTOMATICO
# ISPC
# Listado de opciones:

# 1) Ingreso de dinero
# 2) Extracción de dinero
# 3) Consulta de saldo
# 4) Salir

# Ingrese su selección: _

# El programa deberá mostrar luego del ingreso de cada opción “Usted ha seleccionado la opción x”, por ejemplo, en el caso de ingresar un 1, deberá mostrar por pantalla “Usted ha seleccionado la opción 1” y así sucesivamente. Al seleccionar la opción 4 se debe terminar la ejecución del programa.

# 3) Deberá continuar con el ejercicio 2 y escribir la lógica del cajero automático de la siguiente manera.
# a. Su saldo inicial será de $10000.
# b. Al seleccionar la opción 1 se pedirá al usuario que ingrese un importe por teclado el cual se sumará a su saldo inicial.
# c. De la misma manera al seleccionar la opción 2, se solicitará un importe por teclado el cual se restará al saldo inicial.
# d. Con la opción 3 se consultará su saldo actual.
# e. En todo momento se deberá contralar que no se pueda extraer dinero, si no se cuentan con fondos suficientes.

# 4) Deberá en un solo programa unir el logueo del sistema con los ejercicios 2 y 3. Esto quiere decir que, si el ingreso al sistema es exitoso, se mostrará el menú del cajero automático y el usuario podrá comenzar a operar.

# Opcional 3: Puede incluir parte de la lógica del programa en una o más funciones.

def validar_ingreso():
    intentos = 0
    bloqueado = False

    while intentos < 3 and not bloqueado:
        usuario = input("Ingrese el nombre de usuario: ")
        contraseña = input("Ingrese la contraseña: ")

        if (usuario == "admin" and contraseña == "1234") or (usuario == contraseña):
            print("Ingreso exitoso")
            mostrar_menu()
            break
        else:
            intentos += 1
            print("Ingreso incorrecto. Intentos restantes:", 3 - intentos)

        if intentos == 3:
            bloqueado = True
            print("Cuenta bloqueada")


def mostrar_menu():
    saldo = 10000

    while True:
        print("CAJERO AUTOMATICO")
        print("ISPC")
        print("Listado de opciones:")
        print("1) Ingreso de dinero")
        print("2) Extracción de dinero")
        print("3) Consulta de saldo")
        print("4) Salir")

        seleccion = input("Ingrese su selección: ")

        if seleccion == "1":
            monto = float(input("Ingrese el monto a depositar: "))
            saldo += monto
            print("Usted ha seleccionado la opción 1")

        elif seleccion == "2":
            monto = float(input("Ingrese el monto a extraer: "))
            if monto > saldo:
                print("No cuenta con fondos suficientes")
            else:
                saldo -= monto
                print("Usted ha seleccionado la opción 2")

        elif seleccion == "3":
            print("Su saldo actual es:", saldo)
            print("Usted ha seleccionado la opción 3")

        elif seleccion == "4":
            print("Gracias por utilizar el cajero automático")
            break

        else:
            print("Selección inválida. Intente nuevamente.")


validar_ingreso()
