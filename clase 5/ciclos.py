numeros1 = [59, 58+5, 45-5, 12*2, 33, 55, 109, 78]

for numero in numeros1:
    if numero % 2 == 0:
        print(numero)
    else:
        print('-')

i=0 
while i < len(numeros1):
    if numeros1[i] < 60:
        print (numeros1[i])
    i += 1