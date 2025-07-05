from parser import interpretar_linea
<<<<<<< HEAD
=======

def main():
    with open("examples/ejemplo4.txt") as archivo:
        for linea in archivo:
            interpretar_linea(linea.strip())

if __name__ == "__main__":
    main()

>>>>>>> d19368411d2fcb8c2a3e13783d5cca11bd9701b7
import turtle

with open("examples/ejemplo1.txt") as archivo:
    for linea in archivo:
        interpretar_linea(linea.strip())

turtle.done()