import turtle
from turtle import Turtle, Screen
import random

t = Turtle()
turtle.colormode(255)

# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('hirst.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

color_list = [(195, 8, 69), (231, 54, 132), (194, 164, 15), (112, 178, 214), (199, 77, 15), (216, 162, 101),
              (34, 187, 112), (29, 104, 167), (14, 23, 64),
             (20, 29, 168), (212, 136, 175), (231, 224, 7), (197, 34, 130), (15, 181, 210), (231, 167, 197),
              (126, 189, 163), (10, 48, 29), (40, 131, 75), (141, 217, 203), (61, 22, 10), (60, 13, 27), (108, 91, 210),
              (235, 64, 34), (131, 217, 230), (183, 17, 9)]


def draw_circle():
    t.fillcolor(random.choice(color_list))
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    t.penup()
    t.forward(30)
    t.pendown()


def moving():
    for _ in range(10):
        t.speed('fastest')
        draw_circle()


my_position = 0


for _ in range(10):
    moving()
    t.penup()
    my_position += 40
    t.goto(0, my_position)
    t.pendown()



screen = Screen()
screen.exitonclick()


