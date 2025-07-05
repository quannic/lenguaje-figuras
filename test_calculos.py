# test_calculos.py

from runtime.shapes import calcular_area, calcular_perimetro

print("Área del círculo:", calcular_area("circle", 40))
print("Perímetro del rectángulo:", calcular_perimetro("rectangle", 100, 50))
print("Área del rectángulo:", calcular_area("rectangle", 100, 50))
print("Área del triángulo:", calcular_area("triangle", 40, 30))
print("Perímetro del triángulo:", calcular_perimetro("triangle", 40, 30))
