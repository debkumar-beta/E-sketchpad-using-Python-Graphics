
from turtle import *

t=Turtle()
screen=Screen()

def pen_sizeincrese():
  pensize=t.pensize()+1
  t.pensize(pensize)  
  
def pen_sizedecrese():
  pensize=t.pensize()-1
  t.pensize(pensize)  
    
def t_forward():
    t.forward(10)
    
def t_backward():
    t.backward(10)

def turn_left():
    new_heading=t.heading()+10;
    t.setheading(new_heading)
        
def turn_right():
    new_heading=t.heading()-10;
    t.setheading(new_heading)
def clearscreenn():
    t.clear()
    t.penup()
    t.home()
    t.pendown()
def penu():
    t.penup()
def pend():
    t.pendown()
            
screen.listen()
screen.onkeypress(t_forward,"w")
screen.onkeypress(t_backward,"s")
screen.onkeypress(turn_right,"d")
screen.onkeypress(turn_left,"a")  
screen.onkey(clearscreenn,"c")  
screen.onkey(penu,"u")
screen.onkey(pend,"p")
screen.onkey(pen_sizeincrese,"h")
screen.onkey(pen_sizedecrese,"l")
    
    



mscreen= Screen()
mscreen.exitonclick()
