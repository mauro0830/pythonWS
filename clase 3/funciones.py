def promediar_notas(nota1:float, nota2:float, nota3:float):
    promedio = (nota1 + nota2 + nota3) / 3
    print("El promedio de las notas es: "+str(promedio))

nota1 = float(input('Ingrese la nota 1: '))
nota2 = float(input('Ingrese la nota 2: '))
nota3 = float(input('Ingrese la nota 3: '))
promediar_notas(nota1, nota2, nota3)
