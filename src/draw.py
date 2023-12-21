import math
import io
import time
from PIL import Image
from turtle import (
    Turtle,
    mainloop,
    Screen,
    pencolor,
    speed,
    left,
    getscreen,
    penup,
    pensize,
    hideturtle,
    pendown,
    goto,
    forward,
    backward,
    right,
)


class Draw:
    def __init__(self, row=10, col=10, line_len=10):
        self.rows = row
        self.cols = col
        self.line_len = 720 // (row * 1)

        self.TOP = 0
        self.BOTTOM = 1
        self.LEFT = 2
        self.RIGHT = 3

    # Assuming the direction starts from positive x-axis
    def draw_direction(self, direction):
        if direction == self.TOP:
            left(90)
            forward(self.line_len)
            backward(self.line_len)
            right(90)
        if direction == self.BOTTOM:
            right(90)
            forward(self.line_len)
            backward(self.line_len)
            left(90)
        if direction == self.LEFT:
            backward(self.line_len)
            forward(self.line_len)
        if direction == self.RIGHT:
            forward(self.line_len)

    def display_span_tree(self, span_tree):
        pensize(2)
        speed(8)
        pencolor("red")

        x = -self.rows * self.line_len // 2 + self.line_len // 2
        y = -x
        penup()
        goto(x, y)

        for row in range(self.rows):
            for col in range(self.rows):
                cell = row * self.rows + col
                pendown()

                for direction in range(4):
                    if span_tree[cell][direction] == 1:
                        self.draw_direction(direction)

                if span_tree[cell][self.RIGHT] == 0:
                    penup()
                    forward(self.line_len)

            y -= self.line_len
            penup()
            goto(x, y)

        # mainloop()

    def display_self(self, min_span_tree):
        pensize(2)
        speed(100)
        hideturtle()
        pencolor("black")

        x = -self.rows * self.line_len // 2
        y = -x
        penup()
        goto(x, y)

        for row in range(self.rows):
            for col in range(self.cols):
                cell = row * self.rows + col

                pendown()

                if min_span_tree[cell][self.TOP] == 1:
                    penup()

                forward(self.line_len)
                right(90)
                pendown()

                if min_span_tree[cell][self.RIGHT] == 1 or (
                    cell == len(min_span_tree) - 1
                ):
                    penup()

                forward(self.line_len)
                right(90)
                pendown()

                if min_span_tree[cell][self.BOTTOM] == 1:
                    penup()

                forward(self.line_len)
                right(90)
                pendown()

                if min_span_tree[cell][self.LEFT] == 1 or cell == 0:
                    penup()

                forward(self.line_len)
                right(90)

                penup()
                forward(self.line_len)
            y -= self.line_len
            goto(x, y)
            penup()

        self.save_screenshot()
        mainloop()

    def save_screenshot(self):
        ts = getscreen()
        ps_data = ts.getcanvas().postscript(colormode="color")
        image = Image.open(io.BytesIO(ps_data.encode("utf-8")))
        image.save(f"./gallery/{time.time()}.png", "png")
