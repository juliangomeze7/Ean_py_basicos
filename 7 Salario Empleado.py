salario = float(input("Ingrese su salario mensual: "))
salud = salario * 0.04
pension = salario * 0.04
salarioTotal = salario - salud - pension

print("Este es su descuento por aporte a salud:", salud)
print("Este es su descuento por pensión:", pension)
print("Este es su salario total con descuentos:", salarioTotal)

