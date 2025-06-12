# Importamos todas las funciones necesarias para graficar y calcular
from runtime.shapes import (
    draw_circle, draw_rectangle, draw_triangle, draw_line,
    set_color, move_turtle, rotate_turtle, clear_screen,
    calcular_area, calcular_perimetro
)
from lexer import tokenizar

# Tabla de símbolos para almacenar las variables definidas por el usuario
tabla_simbolos = {}

# Función que resuelve un valor: si es número lo convierte, si es variable la busca
def obtener_valor(token):
    if token.isdigit():
        return int(token)
    return tabla_simbolos.get(token, 0)

# Función que interpreta una línea del lenguaje personalizado
def interpretar_linea(linea):
    tokens = tokenizar(linea)
    if not tokens:
        return

    comando = tokens[0]  # El primer token siempre será el nombre del comando

    # Declarar una variable: let x = 50
    if comando == "let":
        nombre = tokens[1]
        valor = obtener_valor(tokens[3])
        tabla_simbolos[nombre] = valor

    # Dibuja un círculo: circle(x, y, radio)
    elif comando == "circle":
        x = obtener_valor(tokens[2])
        y = obtener_valor(tokens[3])
        r = obtener_valor(tokens[4])
        draw_circle(x, y, r)

    # Dibuja un rectángulo: rectangle(x, y, ancho, alto)
    elif comando == "rectangle":
        x = obtener_valor(tokens[2])
        y = obtener_valor(tokens[3])
        w = obtener_valor(tokens[4])
        h = obtener_valor(tokens[5])
        draw_rectangle(x, y, w, h)

    # Dibuja un triángulo isósceles desde la base: triangle(x, y, base, height)
    elif comando == "triangle":
        x = obtener_valor(tokens[2])
        y = obtener_valor(tokens[3])
        b = obtener_valor(tokens[4])
        h = obtener_valor(tokens[5])
        draw_triangle(x, y, b, h)

    # Dibuja una línea entre dos puntos: line(x1, y1, x2, y2)
    elif comando == "line":
        x1 = obtener_valor(tokens[2])
        y1 = obtener_valor(tokens[3])
        x2 = obtener_valor(tokens[4])
        y2 = obtener_valor(tokens[5])
        draw_line(x1, y1, x2, y2)

    # Cambia el color actual del lápiz: color("red")
    elif comando == "color":
        color = tokens[2].strip('"')
        set_color(color)

    # Mueve la tortuga a una nueva posición: move(x, y)
    elif comando == "move":
        x = obtener_valor(tokens[2])
        y = obtener_valor(tokens[3])
        move_turtle(x, y)

    # Rota la tortuga: rotate(grados)
    elif comando == "rotate":
        angulo = obtener_valor(tokens[2])
        rotate_turtle(angulo)

    # Limpia la pantalla y borra todo: clear()
    elif comando == "clear":
        clear_screen()

    # Calcula y muestra el área de una figura: area(circle, 40)
    elif comando == "area":
        figura = tokens[2]
        valores = [obtener_valor(v) for v in tokens[3:-1]]
        print("Área:", calcular_area(figura, *valores))

    # Calcula y muestra el perímetro de una figura
    elif comando == "perimetro":
        figura = tokens[2]
        valores = [obtener_valor(v) for v in tokens[3:-1]]
        print("Perímetro:", calcular_perimetro(figura, *valores))
