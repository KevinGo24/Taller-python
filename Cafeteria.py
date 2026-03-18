productos = {
    'Cafe' : 4000,
    'Te' : 3500,
    'Jugo' : 5000
}

print('---------  BIENVENIDO A NUESTRO SISTEMA DE VENTAS ------------')
nommbre_producto = str(input('Que bebida quiere : ')).capitalize()
    
if nommbre_producto in productos:
    cantidad = int(input('Ingrese la cantidad que desea llevar: '))
    
    # Buscamos el precio en el diccionario y multiplicamos
    precio_unitario = productos[nommbre_producto]
    total = precio_unitario * cantidad
    
    print(f'El total de su compra de {nommbre_producto} es: ${total}')
else:
    print('Lo sentimos, ese producto no existe en el menú.')