#File name: turtleGames.py
#Format: Camel Case

import turtle as t
import tkinter as tk
import random as r
import threading as th
import time

WIDTH, HEIGHT = 650, 350
FONT = ("Arial", 10, "normal")

#If you're editing this module, remember this;
#supervisor - stays at the origin
#director - goes to the corner of the screen
#player - acts as the one the user controls and 
#enemy/ food [can be used either way really!] - acts as the reciever of the computer smart code...

#Bugs to fix:
# -The stress/overload of the turtle looping system in the class Snake
# -The direction of the turtles when moving in Snake.secondGameLoop()
# -The overall fact that when the snake hits itself it doesn't do anything to the loop at all

helloText = """
Welcome to the Draw Interface 
wasd - is for movement
cipb - to change color, visibility, check current position and going out
"""

class Draw:

    isVisible = True
    isWriting = True
    colorControl = 0
    shapeCount = 0

    def __init__(self, frame):
        #Setup
        self.uniFrame = frame
        canvas = tk.Canvas(self.uniFrame, width= WIDTH*2, height= HEIGHT*2)
        canvas.grid(row= 0, column= 0)
        screen = t.TurtleScreen(canvas)
        self.player, self.supervisor = [t.RawTurtle(canvas)]*2

        #Then set everything in place
        self.supervisor.write(helloText, font= FONT)
        self.supervisor.hideturtle()
        self.player.speed(0)

        #Controls
        screen.listen()
        screen.onkeypress(self.pForward, "w")
        screen.onkeypress(self.pBackward, "s")
        screen.onkeypress(self.pSideLeft, "a")
        screen.onkeypress(self.pSideRight, "d")
        screen.onkeyrelease(self.changeColor, "c")
        screen.onkeyrelease(self.changeVisibility, "i")
        screen.onkeyrelease(self.printPosToScreen, "p")
        screen.onkeyrelease(self.deleteFrame, "b")

    def pForward(self):
        """go forward then check if you've reached the limit of the board"""
        self.player.forward(10)
        self.checkLimit(0)
    
    def pBackward(self):
        """go backwards then check if you've reached the limit of the board"""
        self.player.backward(10)
        self.checkLimit(10)

    def pSideLeft(self):
        """make a 45-degree turn left"""
        self.player.left(45)

    def pSideRight(self):
        """make a 45-degree turn right"""
        self.player.right(45)

    def checkLimit(self, distanceLimit):
        """check if you've reached the limit of the board and don't go any further"""
        x = y = 0
        
        #Do for x - Width
        if self.player.xcor() > WIDTH - distanceLimit:
            x = WIDTH - distanceLimit
        elif self.player.xcor() < -WIDTH + distanceLimit:
            x = -WIDTH + distanceLimit
        else:
            x = self.player.xcor()

        #Do same for y - Height
        if self.player.ycor() > HEIGHT - distanceLimit:
            y = HEIGHT - distanceLimit
        elif self.player.ycor() < -HEIGHT + distanceLimit:
            y = -HEIGHT + distanceLimit
        else:
            y = self.player.ycor()

        #Goto the position decided by both x and y
        self.player.goto(x, y)

    def printPosToScreen(self):
        """This prints the position to the screen by means of the supervisor"""
        self.supervisor.clear()
        self.supervisor.write(f"Position: {self.player.pos()}")

    def changeColor(self):
        """change turtle's color on command..."""
        colorSpectrum = ("red", "yellow", "orange", "green", "brown", "indigo", "purple", "violet")
        self.player.color(colorSpectrum[self.colorControl % 8])
        self.colorControl += 1

    def changeVisibility(self):
        """make to turtle visible and invisible on command..."""
        if self.isVisible == True:
            self.player.hideturtle()
            self.isVisible = False
        else:
            self.player.showturtle()
            self.isVisible = True

    def changePenState(self):
        """to change the status of the pen to either pendown or penup..."""
        if self.isWriting == True:
            self.player.penup()
            self.isWriting = False
        else:
            self.player.pendown()
            self.isWriting = True

    def changeShape(self):
        """to change shape of the player"""
        shapeTemplate = ("square", "classic", "triangle", "rectangle", "circle", "dot")
        self.player.shape(shapeTemplate[self.shapeCount % 6])
        self.shapeCount += 1

    def deleteFrame(self):
        """Go out of the frame..."""
        self.uniFrame.grid_forget()

#Next Class: Crash
class Crash:

    hitWall = False
    running = True
    
    def __init__(self, frame):
        #Setup
        self.uniFrame = frame
        canvas = tk.Canvas(self.uniFrame, width= WIDTH*2, height= HEIGHT*2)
        canvas.grid(row= 0, column= 0)
        screen = t.TurtleScreen(canvas)
        self.player, self.enemy, self.director = [t.RawTurtle(canvas) for _ in range(3)]

        self.director.teleport(-WIDTH + 30, HEIGHT - 30)
        self.director.hideturtle()
        self.player.speed(2)
        self.player.penup()
        self.enemy.penup()
        self.enemy.forward(200)
        self.enemy.shape("square")
        self.player.shape("triangle")
        self.director.write("Start...", font= FONT)
        #We'll use this for the mean-time

        #Controls
        screen.listen()
        screen.onkeyrelease(self.pSideLeft, "a")
        screen.onkeyrelease(self.pSideRight, "d")
        screen.onkeypress(self.replay, "r")
        screen.onkeyrelease(self.deleteFrame, "b")

        #Game Materials
        combo = 0
        count = 0
        self.carWreck()

        #Game Loop
        while self.running:
            self.pForward()
            
            if self.player.distance(self.enemy) < 10:
                count += 1
                comboText = {True: "Combo [+1]: %i"%combo, False: ""}[combo%10 == 0]
                text = {True: "You hit a wall or two not so sure but you hit.", False: "You didn't hit a wall, Welldone bruh."}[self.hitWall]
                self.directorWriting("Car Count: %i - %s"%(count, text))
                self.hitWall = False
                self.carWreck()

    def pForward(self):
        """go forward then check if you've reached the limit of the board"""
        self.player.forward(10)
        self.checkLimit()

    def pSideLeft(self):
        """make a 45-degree turn left"""
        self.player.left(90)

    def pSideRight(self):
        """make a 45-degree turn right"""
        self.player.right(90)

    def checkLimit(self):
        """check if you've reached the limit of the board and don't go any further"""
        x = y = 0
        
        #Do for x - Width
        if self.player.xcor() > WIDTH:
            x = WIDTH
            self.hitWall = True
        elif self.player.xcor() < -WIDTH:
            x = -WIDTH
            self.hitWall = True
        else:
            x = self.player.xcor()

        #Do same for y - Height
        if self.player.ycor() > HEIGHT:
            y = HEIGHT
            self.hitWall = True
        elif self.player.ycor() < -HEIGHT:
            y = -HEIGHT
            self.hitWall = True
        else:
            y = self.player.ycor()

        #Goto the position decided by both x and y
        self.player.goto(x, y)

    def directorWriting(self, text):
        """Makes the director to literally talk..."""
        self.director.clear()
        self.director.write(text)

    def carWreck(self):
        """This makes cars wreck in random places"""
        xPos = r.randrange(-WIDTH + 30, WIDTH - 30)
        yPos = r.randrange(-HEIGHT + 30, HEIGHT - 30)
        self.enemy.teleport(xPos, yPos)

    def replay(self):
        self.running = False
        Crash(self.uniFrame)

    def deleteFrame(self):
        self.running = False
        self.uniFrame.grid_forget()

#Next Class: Tag 
class Tag:

    record = 0
    running = True

    def __init__(self, frame):
        #Setup
        self.uniFrame = frame
        canvas = tk.Canvas(self.uniFrame, width= WIDTH*2, height= HEIGHT*2)
        canvas.grid(row= 0, column= 0)
        self.screen = t.TurtleScreen(canvas)
        self.player, self.enemy, self.director, self.supervisor = [t.RawTurtle(canvas) for _ in range(4)]

        self.director.teleport(-WIDTH + 30, HEIGHT - 30)
        self.director.hideturtle()
        self.supervisor.hideturtle()
        self.enemy.teleport(300, 0)
        self.enemy.penup()
        self.enemy.speed(2)
        self.player.speed(0)
        self.player.penup()

        timer = th.Thread(target= self.timing, args= ())
        gameplay = th.Thread(target= self.gameLoop, args= ())

        timer.start()
        gameplay.start()

    def gameLoop(self):
        #Controls
        self.screen.listen()
        self.screen.onkeypress(self.pSideRight, "Right")
        self.screen.onkeypress(self.pSideLeft, "Left")
        self.screen.onkeyrelease(self.pForward, "Up")
        self.screen.onkeyrelease(self.replay, "r")
        self.screen.onkeyrelease(self.deleteFrame, "b")

        while self.running:
            self.enemy.setheading(self.enemy.towards(self.player))
            self.enemy.forward(10)

            if self.enemy.distance(self.player) <= 10:
                self.running = False

    def pForward(self):
        """go forward then check if you've reached the limit of the board"""
        self.player.forward(10)
        self.checkLimit()

    def pSideLeft(self):
        """make a 45-degree turn left"""
        self.player.left(90)

    def pSideRight(self):
        """make a 45-degree turn right"""
        self.player.right(90)

    def checkLimit(self):
        """check if you've reached the limit of the board and don't go any further"""
        x = y = 0
        
        #Do for x - Width
        if self.player.xcor() > WIDTH:
            x = WIDTH
            self.changePlayer()
        elif self.player.xcor() < -WIDTH:
            x = -WIDTH
            self.changePlayer()
        else:
            x = self.player.xcor()

        #Do same for y - Height
        if self.player.ycor() > HEIGHT:
            y = HEIGHT
            self.changePlayer()
        elif self.player.ycor() < -HEIGHT:
            y = -HEIGHT
            self.changePlayer()
        else:
            y = self.player.ycor()

        #Goto the position decided by both x and y
        self.player.goto(x, y)

    def changePlayer(self):
        """change turtle's color on command..."""
        colorSpectrum = ("red", "yellow", "orange", "green", "brown", "indigo", "purple", "violet")
        shapeTemplate = ("square", "classic", "triangle", "circle")

        self.player.color(colorSpectrum[self.record % 8])
        self.player.shape(shapeTemplate[self.record % 4])
        self.record += 1

    #Will be incoporated in the next version...
    def timing(self):
        i = 0
        while self.running:
            if i < 60:
                time.sleep(1)
                minute = i // 60
                second = i % 60
                self.director.clear()
                self.director.write("%i%i:%i%i"%(minute//10, minute%10, second//10, second%10))
            else:
                break

            i += 1 #increment i

        self.supervisor.clear()
        if i > 59:
            self.supervisor.write("Good Job, Player")
        else:
            self.supervisor.write("Game Over...")

        self.running = False

    def replay(self):
        self.running = False
        Tag(self.uniFrame)

    def deleteFrame(self):
        self.running = False
        self.uniFrame.grid_forget()

class TurtlePlay:

    def __init__(self, frame):

        #Setup
        self.uniFrame = frame
        canvas = tk.Canvas(self.uniFrame, width= WIDTH*2, height= HEIGHT*2)
        canvas.grid(row= 0, column= 0)
        screen = t.TurtleScreen(canvas)
        self.enemy, self.director = [t.RawTurtle(canvas) for i in range(2)]

        screen.listen()
        screen.onkeyrelease(self.deleteFrame, "b")

        #Preparations
        self.director.hideturtle()
        self.enemy.hideturtle()
        self.enemy.speed(0)

        self.director.write("Programmed, Created and Produced: David George")
        self.rectangle()
        self.maintenance()

        self.director.write("Gamers: Paul George, John the beloved George, Emmanuel George")
        self.ellipse()
        self.maintenance()

        self.director.write("Directed and Edited: David George")
        self.straightLine()
        self.maintenance()

        self.director.write("All Glory to God Almighty")
        self.hexagon()
        self.maintenance()

        self.director.write("Trademark of the DPJE winning Team")
        self.triangle()
        self.maintenance()

    def rectangle(self):
        for i in range(1,400,10):
            self.enemy.fd(i)
            self.enemy.rt(90)

    def ellipse(self):
        for a in range(1,200,10):
            self.enemy.circle(a)
            self.enemy.clear()

    def straightLine(self):
        for n in range(50):
            self.enemy.fd(n)
            self.enemy.home()

    def hexagon(self):
        for b in range(1,700,10):
            self.enemy.rt(60)
            self.enemy.fd(b)

    def triangle(self):
        for s in range(1,700,10):
            self.enemy.lt(120)
            self.enemy.fd(s)

    def maintenance(self):
        self.director.clear()
        self.enemy.clear()
        self.enemy.teleport(0, 0)

    def deleteFrame(self):
        self.uniFrame.grid_forget()

#Last Class: Snake
class Snake:

    running = True
    centralSpeed = 1

    def __init__(self, frame):
        """Verdict: Of all game loops I've tried thirdGameLoop() is by far the closest I have to a real snake game...
        The rest of the game loops will remain along side their related methods but i will be using the third one...
        The first game loop looked like i was trying to make all the bodies think independently...
        The second game loop made them look to robotic plus it never really worked and it's slower to implement...
        The third game loop (though it makes them looked like a jampacked lump of meat) it also does a good job in making them feel normal...
        I'm updating this class this week by God's grace..."""
        #Setup
        self.uniFrame = frame
        canvas = tk.Canvas(self.uniFrame, width= WIDTH*2, height= HEIGHT*2)
        canvas.grid(row= 0, column= 0)
        self.screen = t.TurtleScreen(canvas)
        self.food, self.supervisor = [t.RawTurtle(canvas) for i in range(2)]
        self.bodyParts = [t.RawTurtle(canvas)]

        self.supervisor.hideturtle()
        self.bodyParts[0].speed(1)
        self.bodyParts[0].penup()
        self.bodyParts[0].shape("square")
        self.bodyParts[0].color("green")
        self.bodyParts[0].pencolor("black")
        self.food.shape("square")
        self.food.color("red")

        self.thirdGameLoop() #Main Game Loop::

    #The first Game Loop
    def firstGameLoop(self):
        #Controls
        self.screen.listen()
        self.screen.onkeyrelease(self.pSideLeft, "a")
        self.screen.onkeyrelease(self.pSideRight, "d")
        self.screen.onkeyrelease(self.deleteFrame, "b")
        
        count = 1
        i = 0
        self.foodAppear()

        #Main loop
        while self.running:
            if i != 0:
                self.bodyParts[i].forward(10)
                self.bodyParts[i].setheading(self.bodyParts[i].towards(self.bodyParts[(i-1)%count]))
            else:
                self.bodyParts[i].forward(10)
            self.checkLimit()
            
            if self.bodyParts[0].distance(self.food) < 10:
                count += 1
                self.bodyParts.append(self.bodyParts[-1].clone())
                self.bodyParts[-1].backward(10)
                self.updateSpeed()
                self.foodAppear()
                self.supervisor.clear()
                self.supervisor.write("Well done, you earned +1 -> count: %i"%(count-1))
            
            i = (i + 1) % count

    #The second Game Loop ------------------------------------------------------------------
    def secondGameLoop(self):
        #Controls
        self.screen.listen()
        self.screen.onkeyrelease(self.cSideLeft, "Left")
        self.screen.onkeyrelease(self.cSideRight, "Right")
        self.screen.onkeyrelease(self.deleteFrame, "b")
        
        count = 1
        i = 0
        self.command = "r"
        self.foodAppear()

        #Main loop
        while self.running:
            for b in range(len(self.bodyParts)):
                self.bodyParts[b].forward(10)
                if b != 0:
                    if self.command == "r":
                        self.bodyParts[b].right(90)
                    elif self.command == "l":
                        self.bodyParts[b].left(90)
                self.command = "f"
            self.checkLimit()
            
            if self.bodyParts[0].distance(self.food) < 10:
                count += 1
                self.bodyParts.append(self.bodyParts[-1].clone())
                self.bodyParts[-1].backward(10)
                self.updateSpeed()
                self.foodAppear()
                self.supervisor.clear()
                self.supervisor.write("Well done, you earned +1 -> count: %i"%(count-1))
            
            i = (i + 1) % count

    def cSideLeft(self):
        self.bodyParts[0].left(90)
        self.command = "l"

    def cSideRight(self):
        self.bodyParts[0].right(90)
        self.command = "r"
    # ----------------------------------------------------------------------------------

    def thirdGameLoop(self):
        #This will be proceed without any fail...
        self.coordinates = []
        #Controls
        self.screen.listen()
        self.screen.onkeyrelease(self.pSideLeft, "Left")
        self.screen.onkeyrelease(self.pSideRight, "Right")
        self.screen.onkeyrelease(self.deleteFrame, "b")
        
        count = 1
        i = 0
        location = (0, 0)
        self.foodAppear()

        #Main loop
        while self.running:
            checkLength = len(self.bodyParts)

            if checkLength > 1:
                for b in range(checkLength):
                    if b != 0:
                        self.bodyParts[b].goto(*location)
                        location = self.bodyParts[b].pos()
                    else:
                        location = self.bodyParts[0].pos()
                        self.bodyParts[0].forward(10)
            else:
                self.bodyParts[0].forward(10)

            self.checkLimit()
            
            if self.bodyParts[0].distance(self.food) < 10:
                count += 1
                self.bodyParts.append(self.bodyParts[-1].clone()) # Chose clone cuz it's 
                self.bodyParts[-1].backward(20)
                self.updateSpeed()
                self.foodAppear()
                self.supervisor.clear()
                self.supervisor.write("Well done, you earned +1 -> count: %i"%(count-1))
            
            i = (i + 1) % count

    def updateSpeed(self):
        self.centralSpeed += 1
        for b in self.bodyParts:
            b.speed(self.centralSpeed)

    def pSideLeft(self):
        """make a 90-degree turn left"""
        self.bodyParts[0].left(90)

    def pSideRight(self):
        """make a 90-degree turn right"""
        self.bodyParts[0].right(90)

    def checkLimit(self):
        """check if you've reached the limit of the board and don't go any further"""
        x = y = 0
        
        #Do for x - Width
        if self.bodyParts[0].xcor() > WIDTH or self.bodyParts[0].xcor() < -WIDTH or self.bodyParts[0].ycor() > HEIGHT or self.bodyParts[0].ycor() < -HEIGHT:
            self.running = False
            self.supervisor.clear()
            self.supervisor.write("Game Over...Okay self.running is False")

    def foodAppear(self):
        x = r.randrange(-WIDTH + 30, WIDTH - 30)
        y = r.randrange(-HEIGHT + 30, HEIGHT - 30)
        self.food.teleport(x, y)

    def deleteFrame(self):
        self.running = False
        self.uniFrame.grid_forget()

class Start:

    settings = {}
    UNIFONT = ("Arial", 30, "normal")

    def __init__(self, root):
        self.root = root
        self.root.title("Turtle Games")
        self.menuPage()

    def menuPage(self):
        prefColor = "white"

        self.menuFrame = tk.Frame(self.root)
        self.menuFrame.grid(row= 0, column= 0)

        tk.Label(self.menuFrame, text= "Welcome, %s"%self.settings["name"]).grid(row= 0, column= 0, columnspan= 2)
        tk.Label(self.menuFrame, text= " ", padx= 18).grid(row= 1, column= 0)

        for i in range(1, 5):
            tk.Label(self.menuFrame, text= " ").grid(row= i*2, column= 0)
            tk.Label(self.menuFrame, text= " ", padx= 18).grid(row= (i*2)+1, column= 0)

        tk.Button(self.menuFrame, text= "Test area", width= 55, height= 2, bg= prefColor, font= self.UNIFONT, command= self.testArea).grid(row= 1, column= 1)
        tk.Button(self.menuFrame, text= "Crash mayhem", width= 55, height= 2, bg= prefColor, font= self.UNIFONT, command= self.crashMayhem).grid(row= 3, column= 1)
        tk.Button(self.menuFrame, text= "Chase region", width= 55, height= 2, bg= prefColor, font= self.UNIFONT, command= self.chaseRegion).grid(row= 5, column= 1)
        tk.Button(self.menuFrame, text= "Turtle play", width= 55, height= 2, bg= prefColor, font= self.UNIFONT, command= self.turtlePlay).grid(row= 7, column= 1)
        tk.Button(self.menuFrame, text= "Snake game", width= 55, height= 2, bg= prefColor, font= self.UNIFONT, command= self.snakeGame).grid(row= 9, column= 1)

    def gameLink(self):
        self.menuFrame.grid_forget()
        self.gameFrame = tk.Frame(self.root, bg= "white")
        self.gameFrame.grid(row= 0, column= 0)

    def testArea(self):
        self.gameLink()
        Draw(self.gameFrame)
        self.menuFrame.grid()

    def crashMayhem(self):
        self.gameLink()
        Crash(self.gameFrame)
        self.menuFrame.grid()

    def chaseRegion(self):
        self.gameLink()
        Tag(self.gameFrame)
        self.menuFrame.grid()

    def turtlePlay(self):
        self.gameLink()
        TurtlePlay(self.gameFrame)
        self.menuFrame.grid()

    def snakeGame(self):
        self.gameLink()
        Snake(self.gameFrame)
        self.menuFrame.grid()

if __name__ == "__main__":
    root = tk.Tk()
    frame = tk.Frame(root)
    frame.grid(row= 0, column= 0)
    Snake(frame)
    root.mainloop()
    