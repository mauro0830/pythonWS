# El promedio más alto high_average
def high_average(students):
    prom_mayor = 0
    for student in students.values():
        prom_stud = sum(student['notas']) / len(student['notas'])
        if prom_stud > prom_mayor:
            prom_mayor = prom_stud
    print ("El promedio más alto es: " + str (prom_mayor))

# El promedio más bajo low_average
def low_average(students):
    i= 0
    for student in students.values():

        if (student[0]):
            print (student)
    #print ("El promedio menor es: " + str (prom_menor))

students = {'a': {'name':'Juan','notas':[3.1,4.2,4,3.9,3.2]}, 'j': {'name':'Jenny','notas':[4,3.7,4,4,4.2]},\
        'c': {'name':'Ana','notas':[4.1,4.7,4.1,4.9,4.2]}, 'y': {'name':'Pedro','notas':[4,3.7,4,4,4.2]},\
            'x': {'name':'Pablo','notas':[4,3.3,3.4,3.2,3.2]}, 'l': {'name':'Carlos','notas':[3.4,3.8,4.2,4,4.1]},\
                'v': {'name':'Maria','notas':[4.8,4.7,4.6,4.9,4.8]}, 'r': {'name':'Luisa','notas':[4.8,4.7,4.5,4.5,4.9]},\
                    'b': {'name':'Mario','notas':[2.4,3.2,3.1,3.4,4.2]}, 'g': {'name':'Fabio','notas':[2.4,3.2,3.1,3.4,4.2]}}
low_average(students)


# El promedio más bajo low_average
# La nota más alta de todas
# La nota mas baja de todas
# True o False si hay notas repetidas
