genero = input("Ingrese el genero del cotizante F / M: ")
edad= int(input("Ingrese la edad del cotizante: "))
semanas= int(input("Ingrese el número de semanas cotizadas: "))

if genero == "F":
    if edad >= 58:
        if semanas >= 250:
            print("Felicitaciones, es apta para pensionarse!!")
        else:
            print ("No se puede pensionar, le faltan: " + str(250-semanas) + " semana(s)")
    else:    
        print ("No se puede pensionar, le faltan: " + str(58-edad) + " año(s)")
elif genero =="M":
    if edad >= 63:
        if semanas >= 270:
            print("Felicitaciones, es apto para pensionarse!!")
        else:
            print ("No se puede pensionar, le faltan: " + str(270-semanas) + " semana(s)")
    else:    
        print ("No se puede pensionar, le faltan: " + str(63-edad) + "año(s)")
else:
    print("El genero ingresado no es válido, debe ser F o M")