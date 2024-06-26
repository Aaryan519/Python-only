import turtle as tur
import random

tur.speed(5)
tur.tracer(2)
tur.setup(500, 600)
tur.bgcolor("black")

# Function to draw stars
def draw_star(x, y, size, color):
    tur.penup()
    tur.goto(x, y)
    tur.pendown()
    tur.color(color)
    tur.begin_fill()
    for _ in range(5):
        tur.forward(size)
        tur.right(144)
    tur.end_fill()

# Draw stars randomly
num_stars = 10
colors = ['white', 'yellow', 'orange', 'cyan', 'lightgreen', 'lightblue']

for _ in range(num_stars):
    x = random.randint(-250, 250)
    y = random.randint(-300, 300)
    size = random.randint(5, 20)
    color = random.choice(colors)
    draw_star(x, y, size, color)

# Hide the tur cursor
tur.hideturtle()

# Keep the window open until closed manually
tur.done()
