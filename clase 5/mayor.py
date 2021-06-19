import statistics

numeros1 = [59, 58+5, 45-5, 12*2]
numeros2 = [54, 58+5, 45, 12+24]
numeros3 = [54+2, 58+5, 45, 12]
numeros4 = [4, 58+5, 45*2, 12]

promedio1 = statistics.mean(numeros1) 
promedio2 = statistics.mean(numeros2) 
promedio3 = statistics.mean(numeros3) 
promedio4 = statistics.mean(numeros4) 
promedio_maximo = max(promedio4, promedio3, promedio2, promedio1)

print ("Los promedios son: " + str(promedio1) + ", "+ str(promedio2) + ", "+ str(promedio3) + ", "+ str(promedio4))
print ("El promedio máximo es: " + str(promedio_maximo))
