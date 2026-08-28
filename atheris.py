#!/usr/bin/env python
import turtle
from typing import Callable

# So much math! It's like I'm back in school!
def draw_cross(width: int, height: int):
    def draw_axis_half(negative: bool, half_size: float, steps: int):
        for i in range(1, steps + 1):
            if negative:
                turtle.right(90)
            else:
                turtle.left(90)

            turtle.forward(8)

            if negative:
                turtle.write(-i)
            else:
                turtle.write(i)
        
            turtle.left(180)
            turtle.forward(8)

            if negative:
                turtle.right(90)
            else:
                turtle.left(90)
        
            turtle.forward(half_size / steps)


    half_height = turtle.window_height() / 2
    half_width = turtle.window_width() / 2

    # Draw the 0
    turtle.forward(5)
    turtle.write(0)
    turtle.left(180)
    turtle.forward(5)
    turtle.right(90)

    # Go one above the 0 for the upper y-axis
    turtle.forward(half_height / height)

    # Draw upper y-axis
    draw_axis_half(False, half_height, height)

    # Go back home
    turtle.left(180)
    turtle.forward(half_height)

    # Two steps for the lower y-axis
    turtle.forward((half_height / height) * 2)

    # Draw the lower y-axis
    draw_axis_half(True, half_height, height)

    # Go back home
    turtle.left(180)
    turtle.forward(half_height)
    turtle.forward(half_height / height)
    turtle.right(90)
    turtle.forward(half_width / width)

    # Draw right x-axis
    draw_axis_half(False, half_width, width)

    # Go back home
    turtle.left(180)
    turtle.forward(half_width)
    turtle.forward((half_width / width) * 2)

    # Draw left x-axis
    draw_axis_half(True, half_width, width)


def draw_function_crosses(incrs: int, func: Callable[[float], float], color: str = "black"):
    turtle.color(color)
    height = turtle.window_height()
    width = turtle.window_width()

    turtle.teleport((width / incrs) * -incrs, (height / incrs) * func(-incrs))
    step = -incrs
    while step < incrs:
        step += 0.08
        turtle.goto(((width / incrs) * step) * 2, ((height / incrs) * func(step)) * 2)
        turtle.write("x")

    turtle.color("black")


turtle.title("Atheris")
turtle.speed(10000)

draw_cross(4, 16)
draw_function_crosses(4, lambda x: x, "red")
draw_function_crosses(4, lambda x: x ** 2, "green")
draw_function_crosses(4, lambda x: x ** 3, "blue")

turtle.exitonclick()
