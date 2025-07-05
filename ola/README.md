# Lenguaje Figuras

Este proyecto es un lenguaje de programación simple para crear figuras geométricas usando Python y Turtle.

## Estructura del Proyecto

- `lexer.py`: Analizador léxico.
- `parser.py`: Analizador sintáctico.
- `interpreter.py`: Interpreta los comandos.
- `runtime/shapes.py`: Funciones gráficas usando Turtle.
- `examples/`: Archivos de prueba con comandos.

## Comandos Soportados

- `draw_circle(x, y, r)`
- `draw_square(x, y, side)`
- `draw_rectangle(x1, y1, x2, y2)`
- `rotate(angle)`
- `scale(factor)`

## Cómo Ejecutar

```bash
python interpreter.py examples/ejemplo1.txt
```

Al final se abrirá una ventana Turtle mostrando la figura.

## Autor
Joel Seura
Crispy lang
Fundamentos del lenguaje de la programación
Julio 2025

