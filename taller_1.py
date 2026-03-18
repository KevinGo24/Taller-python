Helados = ['vainilla', 'chocolate', 'ron con pasa ']
def Ventas():
    global Helados
    nombre_helado = (input('Que helado desea: '))

    Cantidad = int(input('Cuanto sabores desea: '))

    Helados[nombre_helado] = {
        "tipo de helados" : nombre_helado,
        "cuanto helado desea": Cantidad
    }
    
    ventas = Helados * Cantidad
    
    for Helados, datos in Helados.items():
        print("-"*50)
        print("Producto:", Helados)
        print("Total por producto:", datos["total"])
        print("Cantidad total vendida:", datos["cantidad"])

    print('cantidad de helado', ventas )