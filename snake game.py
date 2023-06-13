import turtle
import random
import time
delay = 0.1
highscore = 0
score = 0
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600 , height=600)
wn.tracer(0)
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("red")
head.penup()
head.goto(0,0)
head.direction = "stop"
food = turtle.Turtle()
food.shape("square")
food.color("green")
food.penup()
food.goto(0,100)
segments=[]
pen = turtle.Turtle()
pen.shape("square")
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score:0       High Score:0" , align = "center" , font = ("Courier",24,"normal"))

def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        y = head.xcor()
        head.sety(x-20)
    if head.direction == "right":
        y = head.xcor()
        head.setx(x+20)
wn.listen()
wn.onkeypress(go_up, "y")
wn.onkeypress(go_down, "h")
wn.onkeypress(go_left, "g")
wn.onkeypress(go_right,"j")

while True:
    wn.update()
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction

wn.mainloop()