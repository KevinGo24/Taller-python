edad = int(input('Digita la edad : '))
if ( 0 <= edad <= 13):
    print('No puedes ingresar, Eres menor de edad')
elif (13 <= edad <= 17):
    print('Bienvenido,eres clase juvenil')
if(18 <= edad <= 59):
    print('Bienvenido, eres clase general ') 
elif (60 <= edad <= 99):
    print('Bienvenido, eres clase senior ')
    