import turtle

wn = turtle.Screen()
wn.title("Donut Clicker")
wn.bgcolor("light blue")

wn.register_shape("donut.gif")

donut = turtle.Turtle()
donut.shape("donut.gif")
donut.speed(0)

clicks = 0

pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0, 150)
pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 36, "bold"))

def clicked(x, y):
    global clicks
    clicks += 1
    pen.clear()
    pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 36, "bold"))

donut.onclick(clicked)


wn.mainloop()