cantidad = float(input("Ingrese la cantidad que quiere depositar: "))
porcentajeIntereses = float(input("Ingrese el porcentaje de intereses (número del 1 al 100): "))
periodo = int(input("Ingrese el periodo de ahorro (en días): "))

valorIntereses = (cantidad * porcentajeIntereses / 100 * periodo) / 360
descuento = valorIntereses * 0.07
netoPagar = valorIntereses + cantidad - descuento

print("Este es tu valor de intereses:", valorIntereses)
print("Este es tu descuento del 7%:", descuento)
print("Este es tu ahorro total:", netoPagar)
