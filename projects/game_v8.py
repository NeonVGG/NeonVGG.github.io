import turtle
import time
import random

clr={1:"blue",2:"red",3:"black",4:"orange",5:"green",6:"purple"}
# window
win= turtle.Screen()
win.title("Pong")
c=random.randint(1,6)
win.bgcolor(clr[c])
win.setup(width=800, height=600)
win.tracer(0)

FONTSIZE = 30
FONT = ("Consolas", FONTSIZE, "normal")

pen = turtle.Turtle()
pen.color("white")
pfont=48
pen.penup()
pen.hideturtle()
pen.write("Pong!",align="center", font=("Consolas",48,"normal"))
pen.penup()
pen.setpos(0,-100)
pen.penup()
pen.hideturtle()
pen.write("\nEnter the players and names in\n python output screen",align="center", font=("Consolas",24,"normal"))
pen.hideturtle()
pen.penup()


def game(diff,ch):

    pen = turtle.Turtle()
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    win.clear()
    c=random.randint(1,6)
    win.bgcolor(clr[c])
    pen.speed(0)
    pen.setpos(0,0)
    pen.penup()
    pen.hideturtle()
    pen.write("Are you Ready?!",align="center", font=("Consolas",48,"normal"))
    time.sleep(0.75)
    win.clear()
    c=random.randint(1,6)
    win.bgcolor(clr[c])
    pen.speed(0)
    pen.penup()
    pen.hideturtle()
    pen.write("Ready!",align="center", font=("Consolas",48,"normal"))
    time.sleep(0.75)
    win.clear()
    c=random.randint(1,6)
    win.bgcolor(clr[c])
    pen.speed(0)
    pen.penup()
    pen.hideturtle()
    pen.write("Set!",align="center", font=("Consolas",48,"normal"))
    time.sleep(0.75)
    win.clear()
    c=random.randint(1,6)
    win.bgcolor(clr[c])
    win.tracer(0)
    pen.speed(0)
    pen.penup()
    pen.hideturtle()
    pen.write("PLAY!",align="center", font=("Consolas",48,"normal"))
    time.sleep(0.75)
    win.clear()
    win.tracer(0)
    c=random.randint(1,6)
    win.bgcolor(clr[c])
    #paddle width-initial
    p1width=5
    p2width=5
    
    entry=True

    def changeentry(): #to exit
        entry=False
        print("GOODBYE")
        turtle.Terminator()
        win.bye()

        #Player 1 - up down don't 
    p1=turtle.Turtle()
    p1.speed(0)
    p1.shape("square")
    p1.color("white")
    p1.shapesize(stretch_wid=p1width, stretch_len=1)
    p1.penup()
    p1.goto(-350,0)

    #Player 2
    p2=turtle.Turtle()
    p2.speed(0)
    p2.shape("square")
    p2.color("white")
    p2.shapesize(stretch_wid=p2width, stretch_len=1)
    p2.penup()
    p2.goto(350,0)

        #initial score
    point1=0
    point2=0

        #Ball -jittery like a crackhead.. but needs to be here to be seen
    ball=turtle.Turtle()
    ball.speed(0)
    ball.shape("circle")
    ball.color("white")
    ball.penup()
    ball.goto(0,0)

        #net needs to be here to be printed
    net=turtle.Turtle()
    net.color("white")
    net.left(90)
    net.forward(400)
    net.goto(0,0)
    net.right(180)
    net.forward(400)

        #movement
    def p1_up():
        y=p1.ycor()
        if y+30>=300:
            p1.sety(300)
        elif y+30<300:
            y+=30
            p1.sety(y)

    def p1_down():
        y=p1.ycor()
        if y-30<=-300:
            p1.sety(-300)
        elif y-30>-300:
         y-=30
         p1.sety(y)

        #movement
    def p2_up():
        y=p2.ycor()
        if y+30>=300:
            p2.sety(300)
        elif y+30<300:
         y+=30 
         p2.sety(y)

    def p2_down():
        y=p2.ycor()
        if y-30<=-300:
            p2.sety(-300)
        elif y-30>-300:
         y-=30
         p2.sety(y)

        #keybind
    win.listen()
    win.onkeypress(p1_up,"w")
    win.onkeypress(p1_down,"s")
    win.onkeypress(p2_up,"Up")
    win.onkeypress(p2_down,"Down")
    win.onkeypress(changeentry,"h")    
    win.title("Pong")
    c=random.randint(1,6)
    win.bgcolor(clr[c])

    if diff==1:
        ball.dx=0.6
        ball.dy=0.6
    elif diff==2:
        ball.dx=0.8
        ball.dy=0.8
    elif diff==3:
        ball.dx=1.2
        ball.dy=1.2

    # Write
    pen=turtle.Turtle()
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0,260)
    pen.write("{} : {}\t\t\t{} : {}".format(player1,point1,player2,point2),align="center", font=("Consolas",18,"normal"))

    serve=0
    t1=ball.dx
    t2=ball.dy
    # Main
    while entry:
        win.update()
        if serve==0:
            ball.dx=t1*random.random()#*random.choice([-1,1])
            ball.dy=t2*random.random()*random.choice([-1,1])
            if abs(ball.dx)<abs(t1):
                if ball.dx<0:
                    ball.dx=ball.dx-t1/2
                else:
                    ball.dx=ball.dx+t1/2
            if abs(ball.dy)<abs(t2):
                if ball.dy<0:
                    ball.dy=ball.dy-t1/2
                else:
                    ball.dy=ball.dy+t1/2
            serve=1
        ball.setx(ball.xcor()+ball.dx)
        ball.sety(ball.ycor()+ball.dy)
        if ch==1: #CPU MODE
            y=ball.ycor()
            p2.sety(y)

        if ball.ycor()>290:
            ball.sety(290)
            ball.dy *=-1

        if ball.ycor()<-290:
            ball.sety(-290)
            ball.dy *=-1

        if ball.xcor()>420:
            ball.goto(0,0)
            time.sleep(2)
            ball.dx *=-1
            serve=0
            point1+=1
            p1width=5+(point1*-0.25) # at 9 it's too small
            p1.shapesize(stretch_wid=p1width, stretch_len=1)
            pen.clear()
            pen.write("{} : {}\t\t\t{} : {}".format(player1,point1,player2,point2),align="center", font=("Consolas",18,"normal"))
            
        if ball.xcor()<-420:
            ball.goto(0,0)
            time.sleep(2)
            ball.dx *=-1
            serve=0
            point2+=1
            p2width=5+(point2*-0.25)
            p2.shapesize(stretch_wid=p2width, stretch_len=1)
            pen.clear()
            pen.write("{} : {}\t\t\t{} : {}".format(player1,point1,player2,point2),align="center", font=("Consolas",18,"normal"))

        if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<p2.ycor()+(p2width*10) and ball.ycor()>p2.ycor()-(p2width*10)):
            ball.setx(340)
            ball.dx*=-1

        if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<p1.ycor()+(p1width*10) and ball.ycor()>p1.ycor()-(p1width*10)):
            ball.setx(-340)
            ball.dx*=-1

        if point1==10:
            pen.goto(0,0)
            win.clear()
            c=random.randint(1,6)
            win.bgcolor(clr[c])
            pen.penup()
            pen.hideturtle()
            pen.write("{} wins!".format(player1),align="center", font=("Consolas",28,"normal"))
            time.sleep(4)
            changeentry()
        elif point2==10:
            pen.goto(0,0)
            win.clear()
            c=random.randint(1,6)
            win.bgcolor(clr[c])
            pen.penup()
            pen.hideturtle()
            pen.write("{} wins!".format(player2),align="center", font=("Consolas",28,"normal"))
            time.sleep(4)
            changeentry()


validclick=False

def onclick_handler1(x, y):
    ix=int(x//1)
    iy=int(y//1)
    diffdict={1:"Easy",2:"Medium",3:"Hard"}
    if -100 < ix < 100:
        if FONTSIZE < iy < FONTSIZE*3:
            diff=1
            validclick=True
        elif -FONTSIZE < iy < FONTSIZE:
            diff=2
            validclick=True
        elif -FONTSIZE*3 < iy < -FONTSIZE:
            diff=3
            validclick=True
        else:
            validclick=False
    else :
        validclick=False
    if validclick==True:
        win.clear()
        pen.setpos(0,-280)
        pen.write("{} chosen".format(diffdict[diff]),align = "center", font=("Consolas",20,"normal"))
        time.sleep(1.75)
        game(diff,ch)

def difficulty():
    win.clear()
    win.title("Pong")
    c=random.randint(1,6)
    win.bgcolor(clr[c])

    pen.setpos(0,200)
    pen.write("Left player keys :W to move up\tS to move down\nRight player keys : Up arrow to move up\tDown arrow to move down\n",align="center",font=30)

    pen.setpos(0, FONTSIZE*2 - FONTSIZE/2)
    pen.write("Easy", align="center", font=FONT)

    pen.setpos(0, -FONTSIZE/2)
    pen.write("Medium", align="center", font=FONT)      

    pen.setpos(0, -FONTSIZE*2 - FONTSIZE/2)
    pen.write("Hard", align="center", font=FONT)

    pen.setpos(0, -250)
    pen.write("Enter an Option", font=FONT)
    #while not validclick:
    win.onscreenclick(onclick_handler1)
    #diff=int(input("Enter difficulty"))
    #win.clear()
    #game(diff,ch)


print("Welcome to pong!\n")
print("1 for 1 player\n2 for 2 players\n3 to Exit")
ch=int(input("Enter your choice : "))
if ch==3:
    print("Exiting....")
    win.bye()
else:
    player1=input("Player 1 Name : ")
    player2="CPU"
    if ch==2:
        player2=input("Player 2 Name : ")
    difficulty()
    #game(2,ch)




