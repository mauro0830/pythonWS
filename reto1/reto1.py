user_sistem= '51593'
pass_sistem= '39515'
print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
user_ingresado = input("Ingrese el usuario por favor: ")
if (user_sistem == user_ingresado):
    pass_ingresado = input("Ingrese la contraseña por favor: ")
    if (pass_ingresado == pass_sistem):
        captcha = 593 + 9
        suma_usuario= int (input("Captcha: Ingrese el resultado de la suma 593 + 9 = "))
        if (suma_usuario == captcha):
            print ("Sesión iniciada")
        else:
            print ("Error")
            exit()
    else:
        print ("Error")
        exit()
else:
    print("Error")
    exit()
