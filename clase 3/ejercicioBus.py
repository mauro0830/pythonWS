"""
    Un bus viaja a 30km/h en promedio, 90km
    recoger pasajeros demora 2 minutos por pasajero
    bajar pasajero demora 1 minuto

    Cuantos minutos demora el bus, dada una cantidad de pasajeros que se subieron
    y otra cantidad de pasajeros que se bajaron
"""
def calcular_tiempo_recorrido(n1:int, n2:int) -> int:
    tiempo_bus= n1*2 + n2 + 180
    return tiempo_bus

pasajeros_suben = int(input("Ingrese la cantidad de pasajeros se subieron al bus: "))
pasajeros_bajan = int(input("Ingrese la cantidad de pasajeros que se bajaron del bus: "))
print('El tiempo total del recorrido del bus es de: ' + str(calcular_tiempo_recorrido(pasajeros_suben, pasajeros_bajan)) + ' minutos')
