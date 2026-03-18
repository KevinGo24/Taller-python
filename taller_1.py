# Usamos un diccionario vacío para guardar las ventas
registro_ventas = {} 

def Ventas():
    # Pedir datos al usuario
    nombre_helado = input('Qué helado desea (vainilla/chocolate/ron con pasa): ').lower()
    cantidad = int(input('Cuántos helados desea: '))
    precio_por_unidad = 2000  # Definimos un precio base

    # Guardar la venta en el diccionario
    # Usamos el nombre del helado como "llave"
    registro_ventas[nombre_helado] = {
        "cantidad": cantidad,
        "total": cantidad * precio_por_unidad
    }
    
    # Mostrar el resumen de todas las ventas
    for helado, datos in registro_ventas.items():
        print("-" * 30)
        print(f"Producto: {helado.capitalize()}")
        print(f"Cantidad vendida: {datos['cantidad']}")
        print(f"Total a pagar: ${datos['total']}")

# Llamar a la función para probar
Ventas()
