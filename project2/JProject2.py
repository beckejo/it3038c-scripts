# Missile Command Game
# Jay Becker IT3038C Project 2
# Coded following TokyoEdtech tutorial
# Runs via Simple Python Game Library, made by TokyoEdtech
# SPGL Documentation on Github: https://github.com/wynand1004/SPGL

# Import Math, Random, & Simple Python Game Library
import spgl
import math
import random



# Create and initialize game object classes
class JayMissile(spgl.Game):
    missilesremaining = 60
    
    def __init__(self, screen_width, screen_height, background_color, title, splash_length):
        spgl.Game.__init__(self, screen_width, screen_height, background_color, title, splash_length)

    def click(self, x, y):
        # choose closest missile to launch
        optimal_missile = None
        optimal_missile_distance = 5000
        for pmissile in pmissiles:
            if pmissile.status == "ready":
                a = pmissile.xcor() - x
                b = pmissile.ycor() - y
                distance = math.sqrt((a**2) + (b**2))
                if distance < optimal_missile_distance:
                    optimal_missile = pmissile
                    optimal_missile_distance = distance
        if optimal_missile:
            optimal_missile.acquire_target(x, y)
            JayMissile.missilesremaining -= 1
        
            
            

class City(spgl.Sprite):
    def __init__(self, shape, color, x, y):
        spgl.Sprite.__init__(self, shape, color, x, y)

    def explode(self):
        self.clear()
        self.penup()
        self.goto(2500, 2500)
        self.status = None


    def tick(self):
        pass

class Silo(spgl.Sprite):
    def __init__(self, shape, color, x, y):
        spgl.Sprite.__init__(self, shape, color, x, y)

    def explode(self):
        self.clear()
        self.penup()
        self.goto(2500, 2500)
        self.status = None

    def tick(self):
        pass

class PMissile(spgl.Sprite):
    def __init__(self, shape, color, x, y):
        spgl.Sprite.__init__(self, shape, color, x, y)
        self.speed = 5
        self.status = "ready"
        self.targetx = 0
        self.targety = 0
        self.size = 0.5
        self.shapesize(0.2, 0.2, 0)
        self.frame = 0
    
       # calculate path to target    
    def acquire_target(self, targetX, targetY):
        if self.status == "ready":
            self.targetx = targetX
            self.targety = targetY
            
            self.dx = self.xcor() - targetX
            if self.dx == 0:
                self.dx = 0.01
            self.dy = self.ycor() - targetY
            self.m = self.dy/self.dx

            self.status = "launched"
            

    def detonate(self):
        self.frame += 1
        if self.frame < 30:
            self.size = self.frame / 10
            self.shapesize((self.frame / 10), (self.frame / 10), 0)
        elif self.frame < 55:
            self.shapesize((60 - self.frame)/10, (60 - self.frame)/10, 0)
        else:
            self.explode()
        
    def explode(self):
        self.clear()
        self.penup()
        self.goto(2500,2500)
        self.status = None

    # move missile    
    def tick(self):
        if self.status == "launched":
            self.pendown()
            self.setx(self.xcor() + (1 / self.m) * self.speed)
            self.sety(self.ycor() + self.speed)

            # See if target was hit
            a = self.xcor()-self.targetx
            b = self.ycor()-self.targety
            targetDistance = math.sqrt((a**2) + (b**2))

            if targetDistance < 5:
                self.status = "detonate"

            if self.ycor() > 1000:
                self.status = "detonate"
            
        if self.status == "detonate":
            self.detonate()




class EMissile(spgl.Sprite):
    def __init__(self, shape, color, x, y):
        spgl.Sprite.__init__(self, shape, color, x, y)
        # set change in x and y and the speed
        self.dx = 0
        self.dy = 0
        self.speed = 2
        self.size = 1
        self.shapesize(self.size, self.size, 0)
        self.pendown()
        self.status = "ready"
        self.targetx = 0
        self.targety = 0
        self.frame = 4


    # calculate path to target    
    def acquire_target(self, target):
        self.targetx = target.xcor()
        self.targety = target.ycor()
        self.dx = self.xcor() - target.xcor()

        if self.dx == 0:
            self.dx = 0.01
        self.dy = self.ycor() - target.ycor()
        self.m = self.dy/self.dx

        self.status = "launched"

    def detonate(self):
        self.frame += 1
        if self.frame < 30:
            self.size = self.frame / 10
            self.shapesize((self.frame / 10), (self.frame / 10), 0)
        elif self.frame < 55:
            self.shapesize((60 - self.frame)/10, (60 - self.frame)/10, 0)
        else:
            self.explode()
        
    def explode(self):
        self.clear()
        self.penup()
        self.goto(2500,2500)
        self.status = None


    # move missile    
    def tick(self):
        if self.status == "launched":
            self.setx(self.xcor() - (1 / self.m) * self.speed)
            self.sety(self.ycor() - self.speed)

            a = self.xcor()-self.targetx
            b = self.ycor()-self.targety
            targetDistance = math.sqrt((a**2) + (b**2))

            if targetDistance < 5:
                self.status = "detonate"
            
        if self.status == "detonate":
            self.detonate()


# Game setup
game = JayMissile(1024, 768, "black", "Jay's Project 2: Missile Command", 7)
game.points = 0
game.numremaining = 60



cities = []
silos = []
pmissiles = []
emissiles = []


# generate cities and silos on the map
for i in range(6):
    cities.append(City("square", "gray", -490 + (i * 195), -250))

for i in range(3):
    silos.append(Silo("circle", "aqua", -350 + (i * 350), -225))


# generate player missiles
for i in range(60):
    if i <20:
        x = -350
    elif i < 40:
        x = 0
    else:
        x = 350
    
    pmissiles.append(PMissile("circle", "yellow", x, -225))

# generate enemy missiles
for i in range(30):
    emissiles.append(EMissile("triangle", "red", random.randint(-600, 600), random.randint(700, 1100)))

for emissile in emissiles:
    if random.randint(0,10) > 7:
        emissile.acquire_target(random.choice(cities))

# Create Scoreboard
scoreboard = spgl.Label("Points: {}   Cities Intact: {}   Silos Intact: {}   Missiles Launched: {}", "aqua", -500, 360)

while True:
    game.tick()

    # Watch for missile on missile collisions
    for pmissile in pmissiles:
        for emissile in emissiles:
            if pmissile.status == "detonate":
                blastRadius = (pmissile.size * 40) / 2
                a = pmissile.xcor() - emissile.xcor()
                b = pmissile.ycor() - emissile.ycor()
                distance = math.sqrt((a**2) + (b**2))
                if distance < blastRadius:
                    emissile.explode()
                    game.points += 100
                    
            

    # Watch for missile on city collisions
    for emissile in emissiles:
        for city in cities:
            if emissile.status == "detonate":
                blastRadius = (emissile.size * 20) / 2
                a = emissile.xcor() - city.xcor()
                b = emissile.ycor() - city.ycor()
                distance = math.sqrt((a**2) + (b**2))
                if distance < blastRadius:
                    city.explode()
                    cities.remove(city)
                    game.points -= 1000

    # Watch for missile on city/silo collisions
        for silo in silos:
            if emissile.status == "detonate":
                blastRadius = (emissile.size * 20) / 2
                a = emissile.xcor() - silo.xcor()
                b = emissile.ycor() - silo.ycor()
                distance = math.sqrt((a**2) + (b**2))
                if distance < blastRadius:
                    silo.explode()
                    silos.remove(silo)
                    game.points -= 50

    # update scoreboard
    scoreboard.update("Points: {}   Cities Intact: {}   Silos Intact: {}   Missiles Remaining: {}".format(game.points, len(cities), len(silos), JayMissile.missilesremaining))