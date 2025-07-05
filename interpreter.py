from parser import interpretar_linea
import turtle

with open("examples/ejemplo1.txt") as archivo:
    for linea in archivo:
        interpretar_linea(linea.strip())

turtle.done()