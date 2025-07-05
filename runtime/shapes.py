
import turtle
import math

t = turtle.Turtle()
t.speed(1)

def set_color(color):
    t.color(color)

def move_turtle(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def rotate_turtle(angulo):
    t.right(angulo)

def clear_screen():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

def draw_circle(x, y, r):
    move_turtle(x, y - r)
    t.circle(r)

def draw_rectangle(x, y, w, h):
    move_turtle(x, y)
    for _ in range(2):
        t.forward(w)
        t.right(90)
        t.forward(h)
        t.right(90)

def draw_triangle(x, y, base, height):
    move_turtle(x, y)
    t.forward(base)
    t.goto(x + base / 2, y + height)
    t.goto(x, y)

def draw_line(x1, y1, x2, y2):
    move_turtle(x1, y1)
    t.goto(x2, y2)

def calcular_area(figura, *parametros):
    if figura == "circle":
        r = parametros[0]
        return math.pi * r ** 2
    elif figura == "rectangle":
        w, h = parametros
        return w * h
    elif figura == "triangle":
        b, h = parametros
        return (b * h) / 2
    else:
        return 0

def calcular_perimetro(figura, *parametros):
    if figura == "circle":
        r = parametros[0]
        return 2 * math.pi * r
    elif figura == "rectangle":
        w, h = parametros
        return 2 * (w + h)
    elif figura == "triangle":
        b, h = parametros
        lado = math.sqrt((b / 2) ** 2 + h ** 2)
        return b + 2 * lado
    else:
        return 0
def done():
    turtle.done()