#import colorgram
import turtle as t
import random

""""Extract colors from an image using colorgram package"""
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append((new_color))
colors_list = [(226, 231, 236), (58, 106, 148), (224, 200, 109), (134, 84, 58), (223, 138, 62), (196, 145, 171), (234, 226, 204), (224, 234, 230), (141, 178, 204), (139, 82, 105), (209, 90, 69), (188, 80, 120), (68, 105, 90), (237, 225, 233), (134, 182, 136), (133, 133, 74), (63, 156, 92), (48, 156, 194), (183, 192, 201), (214, 177, 191), (19, 57, 93), (21, 68, 113), (112, 123, 149), (229, 174, 165), (172, 203, 182), (158, 205, 215), (69, 58, 47), (108, 47, 60), (53, 70, 65), (72, 64, 53)]

""""Drawing spot art using Turtle - Damien Hirst
 https://www.artsy.net/artist-series/damien-hirst-spots"""
t.colormode(255)
timmy = t.Turtle()
timmy.penup()
timmy.speed("fast")

timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)

dot_count = 100
for i in range(1, dot_count + 1):
    timmy.dot(20, random.choice(colors_list))
    timmy.forward(50)

    if i % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

screen = t.Screen()
screen.exitonclick()