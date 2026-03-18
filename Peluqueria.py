Horario = ('mañana','tarde','noche')
Hora = int(input('hora de llegada del cliente: '))
if Hora in range(6,11):
    print(f'Es de: {Horario[0]}' )
elif Hora in range(11,17):
    print(f'Es de: {Horario[1]}')
elif Hora in range(18,22):
    print(f'Es de: {Horario[2]}')
else:
    print('Debe de estar dentro del horario laboral')