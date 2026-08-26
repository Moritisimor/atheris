#!/usr/bin/env python
import turtle

# So much math! It's like I'm back in school!
def draw_cross(incrs: int):
    def draw_axis_half(negative: bool, half_size: float):
        for i in range(1, incrs + 1):
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
        
            turtle.forward(half_size / incrs)


    half_height = turtle.window_height() / 2
    half_width = turtle.window_width() / 2

    # Draw the 0
    turtle.forward(5)
    turtle.write(0)
    turtle.left(180)
    turtle.forward(5)
    turtle.right(90)

    # Go one above the 0 for the upper y-axis
    turtle.forward(half_height / incrs)

    # Draw upper y-axis
    draw_axis_half(False, half_height)

    # Go back home
    turtle.left(180)
    turtle.forward(half_height)

    # Two steps for the lower y-axis
    turtle.forward((half_height / incrs) * 2)

    # Draw the lower y-axis
    draw_axis_half(True, half_height)

    # Go back home
    turtle.left(180)
    turtle.forward(half_height)
    turtle.forward(half_height / incrs)
    turtle.right(90)
    turtle.forward(half_width / incrs)

    # Draw right x-axis
    draw_axis_half(False, half_width)

    # Go back home
    turtle.left(180)
    turtle.forward(half_width)
    turtle.forward((half_width / incrs) * 2)

    # Draw left x-axis
    draw_axis_half(True, half_width)

turtle.title("Atheris")
turtle.speed(10000)
draw_cross(30)
turtle.exitonclick()
