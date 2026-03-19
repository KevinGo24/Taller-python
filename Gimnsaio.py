print ('-'*5 ,'Bienvenido al GymGo','-'*5)

for x in range(1,6):
    nombre = str(input('Escriba su Nombre: '))
    Dias_asistido = int(input('Dia que asistio: '))
    min_promedio = float(input('Minutos entrenados por dia: '))
    Dias_asistido += 1
    if 0 <= Dias_asistido <= 3:
        print('Bajo compromiso')
    elif 3 <= Dias_asistido <= 4:
        print ('Compromiso medio')
    elif Dias_asistido >= 5:
        print ('Compromiso alto')
        