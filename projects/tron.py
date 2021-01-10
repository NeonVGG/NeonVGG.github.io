import turtle

win=turtle.Screen()
win.title("TRON")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

#TRON
tron=turtle.Turtle()
tron.penup()
tron.speed(0)
tron.shape("classic")
tron.pensize(5)
tron.color("cyan")
tron.pendown()
tron.goto(300,0)

def tron_up():
    tron.forward(1)
    
def tron_down():
    tron.forward(0.03)

def tron_left():
    tron.left(90)

def tron_right():
    tron.right(90)

#CLU
clu=turtle.Turtle()
clu.speed(0)
clu.shape("classic")
clu.pensize(5)
clu.color("yellow")
clu.goto(-300,0)

def clu_up():
    clu.forward(1)
    
def clu_down():
    clu.forward(0.03)

def clu_left():
    clu.left(90)

def clu_right():
    clu.right(90)

#keybind
win.listen()
win.onkeypress(tron_up,"Up")
win.onkeypress(tron_down,"Down")
win.onkeypress(tron_left,"Left")
win.onkeypress(tron_right,"Right")
win.onkeypress(clu_up,"w")
win.onkeypress(clu_down,"s")
win.onkeypress(clu_left,"a")
win.onkeypress(clu_right,"d")

#main loop
while True:
    win.update()
    tron.forward(0.06)
    clu.backward(0.075)
