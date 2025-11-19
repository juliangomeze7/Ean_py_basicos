from math import pi

radio = float(input("Introduce el radio del cilindro: "))
altura = float(input("Introduce la altura del cilindro: "))

volumen = pi * (radio ** 2) * altura

print("El volumen del cilindro es", volumen)
