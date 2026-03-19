Servicios = {'masaje', 'facial', 'manicure'}

# Pedimos el servicio al usuario
eleccion = input("¿Qué servicio desea? ").lower() # .lower() lo pasa a minúsculas para evitar errores

# Verificamos si la elección está DENTRO de los servicios
if eleccion in Servicios:
    print(f"¡Confirmado! El servicio de {eleccion} está disponible.")
else:
    print("Lo sentimos, ese servicio no existe en nuestro spa.")
