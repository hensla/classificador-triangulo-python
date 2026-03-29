lado1 = float(input("dê a medida do lado 1 do seu triângulo: "))
lado2 = float(input("dê a medida do lado 2 do seu triângulo: "))
lado3 = float(input("dê a medida do lado 3 do seu triângulo: "))

if lado1 == lado2 and lado2 == lado3:
    print("seu triângulo é equilátero")

elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
    print("seu triângulo é escaleno")

else:
    print("seu triângulo é isósceles")
