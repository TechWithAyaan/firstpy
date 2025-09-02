# print("Ayaan Is My Name")
# print("My Age Is 12. ")
# print("Ayaan HACKER WARNING WARNING")
# print(35+5)
# name = "Ayaan"
# age = 12
# price = 25.99
# print(type(name))
# print(type(age))
# print(type(price))
import turtle
import colorsys

# setup
turtle.bgcolor("black")
turtle.speed(0)
turtle.hideturtle()
turtle.colormode(255)

# color list banani hai
num_colors = 36
colors = []

for i in range(num_colors):
    hue = i / num_colors
    lightness = (50 + 10 * (i % 2)) / 100
    saturation = 1
    rgb = colorsys.hls_to_rgb(hue, lightness, saturation)
    colors.append(tuple(int(c * 255) for c in rgb))

# spiral draw
for i in range(360):
    turtle.color(colors[i % num_colors])
    turtle.forward(i * 2)
    turtle.right(59)

turtle.done()
