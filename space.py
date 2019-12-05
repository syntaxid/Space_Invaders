# Untuk Memainkan Gamenya Install Module Turtle Terlebih Dahulu
# Tested On Windows 10

# Import Module
import turtle
import os
import math
import random

# Screen
wn = turtle.Screen()
wn.title("Space Invaders - Maulana ID")
wn.bgcolor("black")
wn.bgpic("space_invaders_background.gif")

# Register The Shape
turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")


# Credits
def credits():
    turtle.color("white")
    turtle.speed(0)
    turtle.penup()
    turtle.setpos(-650, 200)
    turtle.write("Game Created\nBy Maulana ID", font=("Consolas", 20, "bold",))
    turtle.penup()
    turtle.hideturtle()
credits()

# Border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(2)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# Score
score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()


# Player
player = turtle.Turtle()
player.color("red")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

player_speed = 15

# Enemy
number_enemies = 5
enemies = []

for i in range(number_enemies):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("blue")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(250, 250)
    enemy.setposition(x, y)

enemy_speed = 2
    
# Bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bullet_speed = 40

# Bullet State
bullet_state = "ready"

# Player Moving
def left():
    x = player.xcor()
    x -= player_speed
    if x < -280:
        x = -280
    player.setx(x)

def right():
    x = player.xcor()
    x += player_speed
    if x > 280:
        x = 280
    player.setx(x)

# Bullet Fire
def fire():
    global bullet_state

    if bullet_state is "ready":
        bullet_state = "fire"
        x = player.xcor()
        y = player.ycor() +10
        bullet.setposition(x, y)
        bullet.showturtle()

def collision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-(t2.ycor(),2)))
    if distance < 15:
        return True
    else:
        return False
# Keyboard Bindings
turtle.listen()
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")
turtle.onkey(fire, "space")

# Main Game Loop
while True:

    for enemy in enemies:
        # Enemy Move
        x = enemy.xcor()
        x += enemy_speed
        enemy.setx(x)

        # Move Back And Down
        if enemy.xcor() > 280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemy_speed *= -1

        if enemy.xcor() < -280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemy_speed *= -1

            # Collision
        if bullet.distance(enemy) < 20:
            bullet.hideturtle()
            bullet_state = "ready"
            bullet.setposition(0, -400)
            # Reset Position The Enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            # Update The Score
            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
            
        if player.distance(enemy) < 20:
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over\nGame Created By Maulana ID\nThanks For Playing")
            break


    # Bullet Move
    if bullet_state is "fire":
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)

    if bullet.ycor() > 275:
        bullet.hideturtle()
        bullet_state = "ready"


        


















