#!/usr/bin/env python
import tkinter as tk
from tkinter import messagebox
import turtle
from typing import Callable

# So much math! It's like I'm back in school!
def draw_cross(graph_size: int):
    turtle.setworldcoordinates(-graph_size, -graph_size, graph_size, graph_size)
    turtle.speed(10000000000)

    def draw_axis_half(negative: bool, steps: int):
        for i in range(1, steps + 1):
            if negative:
                turtle.right(90)
            else:
                turtle.left(90)

            turtle.forward(0.25)

            if negative:
                turtle.write(-i)
            else:
                turtle.write(i)
        
            turtle.left(180)
            turtle.forward(0.25)

            if negative:
                turtle.right(90)
            else:
                turtle.left(90)
        
            turtle.forward(1)

    # Draw the 0
    turtle.forward(0.25)
    turtle.write(0)
    turtle.right(180)
    turtle.forward(0.25)

    turtle.right(90)

    # Go one above the 0 for the upper y-axis
    turtle.forward(1)

    # Draw upper y-axis
    draw_axis_half(False, graph_size)

    # Go back home
    turtle.left(180)
    turtle.forward(graph_size)

    # Two steps for the lower y-axis
    turtle.forward(2)

    # Draw the lower y-axis
    draw_axis_half(True, graph_size)

    # Go back home
    turtle.left(180)
    turtle.forward(graph_size)
    turtle.forward(1)
    turtle.right(90)
    turtle.forward(1)

    # Draw right x-axis
    draw_axis_half(False, graph_size)

    # Go back home
    turtle.left(180)
    turtle.forward(graph_size)
    turtle.forward(2)

    # Draw left x-axis
    draw_axis_half(True, graph_size)


def draw_graph(incrs: int, func: Callable[[float], float], color: str = "black"):
    turtle.setworldcoordinates(-incrs, -incrs, incrs, incrs)
    turtle.color(color)
    turtle.speed(0)

    step = -incrs
    turtle.teleport(step, func(step))

    while step < incrs:
        x = step
        y = func(x)
        step += 0.5
        print(f"f({x}) = {y}")

        if x > incrs :
            break
        elif x < -incrs:
            turtle.teleport(x, y)
        else:
            turtle.goto(x, y)

    turtle.color("black")


def draw_button_callback(fun_text: str, graph_size_text: str):
    turtle.title("[Atheris] Graphing...")

    try:
        size = int(graph_size_text)
    except ValueError:
        messagebox.showerror("Error", "Graph size must be an integer!")
        return

    try:
        fun = eval(fun_text)
        draw_cross(size)
        draw_graph(size, fun)
    except Exception as e:
        turtle.bye()
        messagebox.showerror("Error while graphing", str(e))
        return

    turtle.title("[Atheris] Graphing done!")

    turtle.exitonclick()


def main():
    window = tk.Tk()
    window.title("Atheris")
    window.geometry("400x400")
    tk.Label(window, text="Atheris").pack(pady=10)

    tk.Label(window, text="Function term").pack(pady=10)
    fun_text = tk.Entry(window)
    fun_text.pack()

    tk.Label(window, text="Graph size").pack(pady=10)
    graph_size_text = tk.Entry(window)
    graph_size_text.pack()

    tk.Button(
        window,
        text="Draw",
        command=lambda: draw_button_callback(fun_text.get(), graph_size_text.get())
    ).pack(pady=10)

    window.mainloop()
    turtle.bye()


if __name__ == "__main__":
    main()
