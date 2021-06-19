devs = [{'cc': 1540, 'nombre': 'Miguel', 'salario': 2600000,'years':5},
        {'cc': 1556, 'nombre': 'Cristian', 'salario': 2500000,'years':2},
        {'cc': 2556, 'nombre': 'Juan Ignacio', 'salario': 2500000,'years':3},
        {'cc': 1340, 'nombre': 'Nicolas', 'salario': 2400000,'years':4},
        {'cc': 1526, 'nombre': 'Sendy', 'salario': 2400000,'years':5},
        {'cc': 2516, 'nombre': 'Santiago', 'salario': 2600000,'years':5},
        {'cc': 1547, 'nombre': 'David', 'salario': 2500000,'years':3},
        {'cc': 5556, 'nombre': 'Milton', 'salario': 2800000,'years':6},
        {'cc': 5586, 'nombre': 'Jinneth', 'salario': 2800000,'years':2},
        {'cc': 3556, 'nombre': 'Alejandro', 'salario': 2700000,'years':1}]
        
#Ciclo For
dev_mayor = {}
salario_mayor = 0
for dev in devs:
    if dev["salario"] > salario_mayor:
        salario_mayor = dev["salario"]
        dev_mayor = dev
print ("El desarrollador, con mayor salario, está indentificado con CC: " + str(dev_mayor["cc"]) + " , su nombre es: " + dev_mayor["nombre"] + " y su salario es: " + str(dev_mayor["salario"]))

#Ciclo While
i=0
while i< len(devs):
    if i == 0:
        menor_exp = devs[i]['years']
    if devs[i]["years"] < menor_exp:
        menor_exp = devs[i]["years"]
    i += 1
print ("El desarrollador con menor experiencia tiene: " + str(menor_exp) + " año(s) de experiencia")