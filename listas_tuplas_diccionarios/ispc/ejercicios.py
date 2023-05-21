# 1. Diseña un algoritmo que introduzca por teclado el nombre de 3 países, se almacenen en una lista y los muestre por pantalla.

# pais = input("Ingrese un país: ")
# pais1 = input("Ingrese un país: ")
# pais2 = input("Ingrese un país: ")
# lista_paises=[pais, pais1, pais2]
# print(lista_paises)

# 2. Diseña un algoritmo que almacene los precios de 4 productos que compré en una lista y luego me muestre el total en pantalla.

# productos=[450,500,550,600]
# suma_productos=sum(productos)
# print("El total de la compra es " + suma_productos)

# 3. Diseña un algoritmo que almacene las letra de tu nombre en una lista y luego muestre el nombre.
# letras_nombre=("I", "v", "e", "t", "t", "e")
# nombre="".join(letras_nombre)
# print(nombre)

# 4. Diseña un algoritmo que introduzca por teclado el nombre, materia, profesor y nota. Se almacene en una tupla y luego muestre los datos en pantalla.

# nombre = input("Introduzca su nombre: ")
# materia = input("Introduzca la materia: ")
# profesor = input("Introduzca el nombre del profesor: ")
# nota = input("Introduzca la nota: ")


# 5. Diseña un algoritmo que introduzca por teclado el nombre de 3 materias y sus notas correspondientes. Deben almacenarse las materias en una tupla
# y las notas en otra. Luego muestre en pantalla la materia con su nota correspondiente.
# materia1 = input("Materia: ")
# nota1 = input("Nota: ")
# materia2 = input("Materia: ")
# nota2 = input("Nota: ")
# materia3 = input("Materia: ")
# nota3 = input("Nota: ")

# tupla_materias = (materia1, materia2, materia3)
# tupla_notas = (nota1, nota2, nota3)
# print(tupla_materias[0], ": ", tupla_notas[0])
# print(tupla_materias[1], ": ", tupla_notas[1])
# print(tupla_materias[2], ": ", tupla_notas[2])

# 6. Diseña un algoritmo con un diccionario que contenga como clave 3 materias que estás cursando y como valores uses tuplas para almacenar
# 2 notas por materia. Luego por pantalla muestres las notas de cada materia.
# diccionario_materias = {
#     "Materia1": (7, 8),
#     "Materia2": (7, 8),
#     "Materia3": (7, 8)
# }

# print(diccionario_materias["Materia1"],
#       diccionario_materias["Materia2"],
#       diccionario_materias["Materia3"])

# 7. Diseña un algoritmo creando una tupla que almacene 3 categorías de música y luego crea un diccionario donde utilices como clave la tupla
# y almacenes 2 músicos por categoría de música. Luego mostrar en pantalla los artistas.
# categoria_musica = ("Rock", "Alternativo", "Jazz")
# diccionario_musica = {"Rock": ["Queen", "AC/DC"], "Alternativo": [
#     "Coldplay", "Keane"], "Jazz": ["Monk", "Armstrong"]}
# print(diccionario_musica["Alternativo"],
#       diccionario_musica["Rock"],
#       diccionario_musica["Jazz"])

# 8. Realice un programa que cambie pesos a dólares. Mejórelo, añadiendo el cambio de dólares a pesos y que sea el usuario quién decida qué tipo
# de cambio quiere, si de dólares a pesos o viceversa.


moneda = input("Tipo de moneda a convertir: ")

if moneda.lower() == "dolar":
    cantidad = int(input("Monto a convertir: "))
    conversion = input("¿A que moneda lo queres convertir?: ")
    if conversion.lower() == "pesos":
        resultado_conversion = cantidad/227.5
        print(cantidad, " dolares son ", resultado_conversion, "pesos")

if moneda.lower() == "pesos":
    cantidad2 = int(input("Monto a convertir: "))
    conversion2 = input("¿A que moneda lo queres convertir?")
    if conversion2.lower() == "dolar":
        resultado_conversion2 = cantidad2*227.5
        print(cantidad2, "pesos son ", resultado_conversion2, "dolares")

else:
    print("Gracias por usar nuestra calculadora de moneda extranjera")
