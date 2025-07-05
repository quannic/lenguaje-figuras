
from runtime.shapes import (
    draw_circle, draw_rectangle, draw_triangle, draw_line,
    set_color, move_turtle, clear_screen, rotate_turtle,
    calcular_area, calcular_perimetro
)
from lexer import tokenizar

tabla_simbolos = {}

def obtener_valor(token):
    if token.isdigit():
        return int(token)
    return tabla_simbolos.get(token, 0)

def interpretar_linea(linea):
    tokens = tokenizar(linea)
    if not tokens:
        return

    comando = tokens[0]

    if comando == "let":
        nombre = tokens[1]
        valor = obtener_valor(tokens[3])
        tabla_simbolos[nombre] = valor

    elif comando == "circle":
        x = obtener_valor(tokens[1])
        y = obtener_valor(tokens[2])
        r = obtener_valor(tokens[3])
        draw_circle(x, y, r)

    elif comando == "rectangle":
        x = obtener_valor(tokens[1])
        y = obtener_valor(tokens[2])
        w = obtener_valor(tokens[3])
        h = obtener_valor(tokens[4])
        draw_rectangle(x, y, w, h)

    elif comando == "triangle":
        x = obtener_valor(tokens[1])
        y = obtener_valor(tokens[2])
        b = obtener_valor(tokens[3])
        h = obtener_valor(tokens[4])
        draw_triangle(x, y, b, h)

    elif comando == "line":
        x1 = obtener_valor(tokens[1])
        y1 = obtener_valor(tokens[2])
        x2 = obtener_valor(tokens[3])
        y2 = obtener_valor(tokens[4])
        draw_line(x1, y1, x2, y2)

    elif comando == "color":
        color = tokens[1].strip('"')
        set_color(color)

    elif comando == "move":
        x = obtener_valor(tokens[1])
        y = obtener_valor(tokens[2])
        move_turtle(x, y)

    elif comando == "rotate":
        angulo = obtener_valor(tokens[1])
        rotate_turtle(angulo)

    elif comando == "clear":
        clear_screen()

    elif comando == "area":
        figura = tokens[1]
        valores = [obtener_valor(v) for v in tokens[2:]]
        print("Área:", calcular_area(figura, *valores))

    elif comando == "perimetro":
        figura = tokens[1]
        valores = [obtener_valor(v) for v in tokens[2:]]
        print("Perímetro:", calcular_perimetro(figura, *valores))
