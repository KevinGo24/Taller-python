# 1. Pedir el dato al usuario
horas = int(input("¿Cuántas horas estuvo  en el parqueadero?: "))

# 2. Lógica con condicionales
if horas <= 0:
    total = 0
    print("Tiempo no válido.")
elif horas == 1:
    # Caso base: Solo la primera hora
    total = 5000
else:
    # Caso horas adicionales:
    # La primera cuesta 5000, y a las demás (horas - 1) se les cobra 3000
    total = 5000 + (horas - 1) * 3000

# 3. Mostrar resultado
if horas > 0:
    print(f"Total a pagar por {horas} horas: ${total}")
