
from parser import interpretar_linea

def main():
    with open("examples/ejemplo1.txt") as archivo:
        for linea in archivo:
            interpretar_linea(linea.strip())

if __name__ == "__main__":
    main()

import turtle
turtle.done()
