
import turtle
import math

# Inicializa la pantalla y la tortuga (pincel)
pantalla = turtle.Screen()
pantalla.bgcolor("white")
pincel = turtle.Turtle()
pincel.speed(0)

# Función para cambiar el color del trazo
def set_color(color):
    pincel.color(color)

# Mueve la tortuga a una posición sin dibujar
def move_turtle(x, y):
    pincel.penup()
    pincel.goto(x, y)
    pincel.pendown()

# Rota la tortuga a la derecha (en grados)
def rotate_turtle(angulo):
    pincel.right(angulo)

# Borra todo lo que hay en pantalla
def clear_screen():
    pincel.clear()
    pincel.penup()
    pincel.home()
    pincel.pendown()

# Dibuja un círculo: centro (x, y) y radio
def draw_circle(x, y, r):
    move_turtle(x, y - r)
    pincel.circle(r)

# Dibuja un rectángulo desde la esquina superior izquierda
def draw_rectangle(x, y, w, h):
    move_turtle(x, y)
    for _ in range(2):
        pincel.forward(w)
        pincel.right(90)
        pincel.forward(h)
        pincel.right(90)

# Dibuja un triángulo isósceles centrado en la base
def draw_triangle(x, y, base, height):
    move_turtle(x, y)
    pincel.forward(base)
    pincel.goto(x + base / 2, y + height)
    pincel.goto(x, y)

# Dibuja una línea entre dos puntos
def draw_line(x1, y1, x2, y2):
    move_turtle(x1, y1)
    pincel.goto(x2, y2)

# Calcula el área de figuras geométricas
def calcular_area(figura, *parametros):
    if figura == "circle":
        r = parametros[0]
        return math.pi * r**2
    elif figura == "rectangle":
        w, h = parametros
        return w * h
    elif figura == "triangle":
        base, altura = parametros
        return (base * altura) / 2
    else:
        return 0

# Calcula el perímetro de figuras geométricas
def calcular_perimetro(figura, *parametros):
    if figura == "circle":
        r = parametros[0]
        return 2 * math.pi * r
    elif figura == "rectangle":
        w, h = parametros
        return 2 * (w + h)
    elif figura == "triangle":
        base, altura = parametros
        # Aproximación asumiendo triángulo isósceles
        lado = math.sqrt((base / 2)**2 + altura**2)
        return base + 2 * lado
    else:
        return 0
