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

 
pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0, 200)
pen.write(f"Clicks: {clicks}", align="center", font=("Comic Sans", 32))

pen1 = turtle.Turtle()
pen1.hideturtle()
pen1.color("white")
pen1.penup()
pen1.write(f"Cost: {cursor_price}", pen1.goto(-520, 300), font=("Comic Sans", 32))

pen2 = turtle.Turtle()
pen2.hideturtle()
pen2.color("white")
pen2.penup()
pen2.write(f"Cost: {grandma_price}", pen2.goto(300, 300), font=("Comic Sans", 32))
 
def clicked(x, y):
    global clicks
    clicks += cursor_multiplier
    pen.clear()
    pen.write(f"Clicks: {clicks}", align="center", font=("Comic Sans", 32))
 
def buy_cursor(x, y):
    global clicks, cursor_price, cursor_multiplier
    if clicks >= cursor_price:
        clicks -= cursor_price
        cursor_multiplier += 1
        cursor_price += 50
        pen.clear()
        pen1.clear()
        pen1.write(f"Cost: {cursor_price}", pen1.goto(-520, 300), font=("Comic Sans", 32))
        pen.write(f"Clicks: {clicks}", align="center", font=("Comic Sans", 32))
 
def buy_grandma(x, y):
    global clicks, grandma_price, grandma_clicks
    if clicks >= grandma_price:
        clicks -= grandma_price
        grandma_clicks += 1
        grandma_price += 100
        pen.clear()
        pen2.clear()
        pen2.write(f"Cost: {grandma_price}", pen2.goto(300, 300), font=("Comic Sans", 32))
        pen.write(f"Clicks: {clicks}", align="center", font=("Comic Sans", 32))
        wn.ontimer(grandma_click, 1000)
 
def grandma_click():
    global clicks, grandma_clicks
    clicks += grandma_clicks
    pen.clear()
    pen.write(f"Clicks: {clicks}", align="center", font=("Comic Sans", 32))
    wn.ontimer(grandma_click, 1000)
 
cookie.onclick(clicked)
cursor.onclick(buy_cursor)
grandma.onclick(buy_grandma)
 
wn.mainloop()