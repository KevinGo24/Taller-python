Asistencia = [' baja', ' media', ' alta']

Users = int(input('Asistencia por clase: '))

if Users in range(0,5):
    print (f'Su asistencia es: {Asistencia[0]}')
if Users in range(5,8):
    print (f'Su asistencia es: {Asistencia[1]}')
if Users in range(9,70):
    print (f'Su asistencia es: {Asistencia[2]}')