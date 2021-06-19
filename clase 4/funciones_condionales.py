def verificar_mayor(edad1, edad2, edad3, edad4):
    if edad1>edad2 and edad1>edad3 and edad1>edad4:
        print ("La mayor edad es: " + str(edad1))
    elif edad2>edad1 and edad2>edad3 and edad2>edad4:
        print ("La mayor edad es: " + str(edad2))
    elif edad3>edad1 and edad3>edad2 and edad3>edad4:
        print ("La mayor edad es: " + str(edad3))
    elif edad4>edad1 and edad4>edad2 and edad4>edad2: 
        print ("La mayor edad es: " + str(edad4))

edad1= int(input("Ingrese la primera edad: "))
edad2= int(input("Ingrese la segunda edad: "))
edad3= int(input("Ingrese la tercera edad: "))
edad4= int(input("Ingrese la cuarta edad: "))
verificar_mayor(edad1,edad2,edad3,edad4)