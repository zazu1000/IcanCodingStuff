import turtle
import time
 
wn = turtle.Screen()
wn.bgcolor("green")
 
wn.register_shape(r"C:\Users\iCan Student\Downloads\cookie.gif")
wn.register_shape(r"C:\Users\iCan Student\Downloads\cursor.gif")
wn.register_shape(r"C:\Users\iCan Student\Downloads\grandma.gif")
 
cookie = turtle.Turtle()
cookie.shape(r"C:\Users\iCan Student\Downloads\cookie.gif")
cookie.speed(0)
 
cursor = turtle.Turtle()
cursor.shape(r"C:\Users\iCan Student\Downloads\cursor.gif")
cursor.speed(0)
cursor.penup()
cursor.goto(-400, 0)
cursor_price = 50
cursor_multiplier = 1
 
grandma = turtle.Turtle()
grandma.shape(r"C:\Users\iCan Student\Downloads\grandma.gif")
grandma.speed(0)
grandma.penup()
grandma.goto(400, 0)
grandma_price = 100
grandma_clicks = 0
 
clicks = 0
cursor_tracker = 0
grandma_tracker = 0

pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0, 200)
pen.write(f"Money: {clicks}" + "$", align="center", font=("Comic Sans", 32))

cp = turtle.Turtle()
cp.hideturtle()
cp.color("white")
cp.penup()
cp.write(f"Cost: {cursor_price}" + "$", cp.goto(-520, 300), font=("Comic Sans", 32))

gp = turtle.Turtle()
gp.hideturtle()
gp.color("white")
gp.penup()
gp.write(f"Cost: {grandma_price}" + "$", gp.goto(300, 300), font=("Comic Sans", 32))

ct = turtle.Turtle()
ct.hideturtle()
ct.color("white")
ct.penup()
ct.write(f"Amount: {cursor_tracker}", ct.goto(-520, -300), font=("Comic Sans", 32))

gt = turtle.Turtle()
gt.hideturtle()
gt.color("white")
gt.penup()
gt.write(f"Amount: {grandma_tracker}", gt.goto(300, -300), font=("Comic Sans", 32))

error = turtle.Turtle()
error.hideturtle()
error.color("white")
error.penup()

 
def clicked(x, y):
    global clicks
    clicks += cursor_multiplier
    pen.clear()
    pen.write(f"Money: {clicks}" + "$", align="center", font=("Comic Sans", 32))
 
def buy_cursor(x, y):
    global clicks, cursor_price, cursor_multiplier, cursor_tracker
    if clicks >= cursor_price:
        clicks -= cursor_price
        cursor_multiplier += 1
        cursor_price += 50
        cursor_tracker += 1
        pen.clear()
        pen.write(f"Money: {clicks}" + "$", align="center", font=("Comic Sans", 32))
        cp.clear()
        cp.write(f"Cost: {cursor_price}" + "$", cp.goto(-520, 300), font=("Comic Sans", 32))
        ct.clear()
        ct.write(f"Amount: {cursor_tracker}", ct.goto(-520, -300), font=("Comic Sans", 32))
    else:
        error.write("Error: Funds not sufficient", error.goto(-190, -300), font=("Comic Sans", 25))
        time.sleep(3)
        error.clear()
 
def buy_grandma(x, y):
    global clicks, grandma_price, grandma_clicks, grandma_tracker
    if clicks >= grandma_price:
        clicks -= grandma_price
        grandma_clicks += 1
        grandma_price += 100
        grandma_tracker += 1
        pen.clear()
        pen.write(f"Money: {clicks}" + "$", align="center", font=("Comic Sans", 32))
        gp.clear()
        gp.write(f"Cost: {grandma_price}" + "$", gp.goto(300, 300), font=("Comic Sans", 32))
        gt.clear()
        gt.write(f"Amount: {grandma_tracker}", gt.goto(300, -300), font=("Comic Sans", 32))
        wn.ontimer(grandma_click, 1000)
    else:
        error.write("Error: Funds not sufficient", error.goto(-190, -300), font=("Comic Sans", 25))
        time.sleep(3)
        error.clear()
 
def grandma_click():
    global clicks, grandma_clicks
    clicks += grandma_clicks
    pen.clear()
    pen.write(f"Money: {clicks}" + "$", align="center", font=("Comic Sans", 32))
    wn.ontimer(grandma_click, 1000)
 
cookie.onclick(clicked)
cursor.onclick(buy_cursor)
grandma.onclick(buy_grandma)
 
wn.mainloop()