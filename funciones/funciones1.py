# Resolver los siguientes ejercicios usando funciones

# 1.Realice una función para calcular el costo total recaudado en entradas de un recital.

# def recaudacion(entradas_vendidas, valor_entrada):
#     costo_total = entradas_vendidas * valor_entrada
#     return costo_total
# valor_entrada = 9000
# entradas_vendidas = 25000

# costo_total = recaudacion(entradas_vendidas, valor_entrada)

# print(f'El costo total recaudado es de: {costo_total} pesos.')


# 2.Función para comprobar si una canción está en la lista de reproducción de un recital.

# def cancion_playlist(playlist, cancion):
#     if cancion in playlist:
#         return True
#     else:
#         return False


# playlist = ["Viva La Vida", "A Sky Full of Stars",
#             "Magic", "Fix You", "Yellow", "Clocks"]
# cancion = "Clocks"

# if cancion_playlist(playlist, cancion):
#     print("La canción está en la lista de reproducción.")
# else:
#     print("La canción no está en la lista de reproducción.")

# 3.Función para calcular el tiempo total de duración de un recital, considerando la duración de x cantidad de canciones.

# def duracion_recital(duracion_cancion, cantidad_canciones):
#     duracion_total = duracion_cancion * cantidad_canciones
#     return duracion_total


# duracion_cancion = 4
# cantidad_canciones = 12

# duracion_total = duracion_recital(duracion_cancion, cantidad_canciones)
# print(f'La duración total del recital es de {duracion_total} minutos')

# 4.Crear una función que calcule la velocidad promedio de un auto, dada la distancia recorrida y el tiempo empleado.

# def velocidad_promedio(distancia, tiempo):
#     velocidad = distancia / tiempo
#     return velocidad


# distancia = 2000
# tiempo = 18

# velocidad = velocidad_promedio(distancia, tiempo)

# print(f'La velocidad promedio del auto es de {velocidad} km/hora.')

# 5.Crear una función que determine si un auto está en marcha o detenido, dada su velocidad.


# def auto_en_marcha(velocidad):
#     if velocidad == 0:
#         auto = "detenido"
#     else:
#         auto = "en marcha"
#     return auto


# velocidad = 0
# auto = auto_en_marcha(velocidad)

# print(f'El auto está {auto}')

# 6.Crear una función que convierta kilómetros por hora a millas por hora.

# def convertidor_medidas(kilometros):
#     millas_por_hora = kilometros * 0.621371
#     return millas_por_hora


# kilometros = 120
# millas_por_hora = convertidor_medidas(kilometros)
# print(f'{kilometros} kmph equivalen a {millas_por_hora} mph')

# 7.Crear una función que calcule el consumo de combustible de un auto por kilómetro, dada la distancia recorrida
# y la cantidad de combustible utilizada.

# def consumo_combustible_km(distancia, combustible_total):
#     combustible_km = combustible_total / distancia
#     return combustible_km


# distancia = 100
# combustible_total = 25

# combustible_km = consumo_combustible_km(distancia, combustible_total)

# print(f'El consumo de combustible por km es de {combustible_km} litros')

# 8.Crear una función que determine el costo de un viaje en auto, dada la distancia recorrida, el consumo de combustible y
# el precio del combustible.

def costo_viaje(distancia, combustible, precio_combustible):
    costo = distancia * combustible * precio_combustible
    return costo


distancia = 800
combustible = 0.10
precio_combustible = 120

costo = costo_viaje(distancia, combustible, precio_combustible)

print(f'El costo total del viaje en auto es de ${costo}')
