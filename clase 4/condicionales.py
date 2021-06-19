edad_jugador = int(input("Ingrese la edad del jugador: "))

if edad_jugador >= 10 and edad_jugador <= 14:
    print("El jugador es categoria infantil.")
elif edad_jugador >= 15 and edad_jugador <= 17:
    print("El jugador es categoria juvenil.")
elif edad_jugador >= 18 and edad_jugador <= 20:
    print("El jugador es categoria Sub20.")
elif edad_jugador > 20:
    print("El jugador es categoria Profesional.")
else: 
    print("El jugador no aplica categoria, muy joven.")
