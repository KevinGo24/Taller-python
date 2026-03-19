prendas_caras = 0
precio_max = 0
posicion_mayor = 0  # Mostar al usuario el producto mas alto 

for x in range(1, 7): # mostar al usuario los 6 producto 
    precio = float(input(f'Precio del producto {x}: '))
    
    # 1. Cuenta los que valen más de 100,000
    if precio > 100000:
        prendas_caras += 1
        
    # 2. Guarda el precio más alto Y su número de producto (x)
    if precio > precio_max:
        precio_max = precio
        posicion_mayor = x # Guardamos si fue el 1, el 2, etc.

print(f'\nCantidad de productos caros (>100k): {posicion_mayor}')
print("="*10)
print(f'El producto más caro fue el número {posicion_mayor} con un precio de: {precio_max}')

