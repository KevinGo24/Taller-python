Tipo_helado = {
    'Cono': 3000,
    'Vaso': 4000,
    'Banana split': 9000
}

# Inicializamos acumuladores y contadores
total_ventas = 0
total_clientes = 0
conteo_productos = {'Cono': 0, 'Vaso': 0, 'Banana split': 0}

print('---------  BIENVENIDO A HELADERIA FANTASYGO  ------------')

continuar = "si"
while continuar.lower() == "si":
    print("\nMenú:", list(Tipo_helado.keys()))
    producto = input('¿Qué producto desea?: ').capitalize() # Capitalize para que coincida con el Diccionario

    if producto in Tipo_helado:
        cantidad = int(input(f'¿Cuántos {producto} desea?: '))
        
        # Calcular total del cliente
        subtotal = Tipo_helado[producto] * cantidad
        total_ventas += subtotal
        total_clientes += 1
        conteo_productos[producto] += cantidad # Contamos cuántas veces se pidió
        
        print(f'Total a pagar: ${subtotal}')
    else:
        print("Producto no válido.")

    continuar = input('\n¿Desea registrar otro cliente? (si/no): ')

# Calcular cuál se pidió más
producto_mas_vendido = max(conteo_productos, key=conteo_productos.get)

print('\n' + '='*40)
print(f'Total vendido en el día: ${total_ventas}')
print(f'Clientes atendidos: {total_clientes}')
print(f'El producto más pedido fue: {producto_mas_vendido}')
