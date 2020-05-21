import turtle
import time # for the timer module
import random

delay = 0.01
score = 0
high_score = 0

# setting up the screem
wn = turtle.Screen()
wn.title("Snake Game by @Rohit0718")
wn.bgcolor("blue")
wn.setup(width = 600, height = 600)
wn.tracer(0) # turns off screen updates

# creating the snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup() # turning off line drawing by the turlte
head.goto(0,0)
head.direction = "right"

# creating the food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup() # turning off line drawing by the turlte
food.goto(0,100)

segments = [head]

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High score: 0", align = "center", font = ("Courier", 24, "normal"))

# functions

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
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

def collides(x, y):
    for s in segments:
        if s.xcor() == x and s.ycor() == y:
            return True
    return False

# keyboard bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_right, "Right")
wn.onkeypress(go_left, "Left")

INF = 100000000

# main game loop
while True:
    wn.update()

    # best first search
    
    ## calculate all possible vals of next state
    cur_up = (head.xcor(), head.ycor() + 20) if (head.ycor() <= 260 and not collides(head.xcor(), head.ycor() + 20)) else (INF, INF)
    cur_down = (head.xcor(), head.ycor() - 20) if (head.ycor() >= -260 and not collides(head.xcor(), head.ycor() - 20)) else (INF, INF)
    cur_right = (head.xcor() + 20, head.ycor()) if (head.xcor() <= 260 and not collides(head.xcor() + 20, head.ycor())) else (INF, INF)
    cur_left = (head.xcor() - 20, head.ycor()) if (head.xcor() >= -260 and not collides(head.xcor() - 20, head.ycor())) else (INF, INF)
    
    ## apply manhattan distance heuristic on all four possibilities
    man_dist_up = abs(food.xcor() - cur_up[0]) + abs(food.ycor() - cur_up[1])
    man_dist_down = abs(food.xcor() - cur_down[0]) + abs(food.ycor() - cur_down[1])
    man_dist_right = abs(food.xcor() - cur_right[0]) + abs(food.ycor() - cur_right[1])
    man_dist_left = abs(food.xcor() - cur_left[0]) + abs(food.ycor() - cur_left[1])

    ## obtain index of move with lowest manahttan distance heuristic 
    v, i = min((v, i) for (i, v) in enumerate([man_dist_up, man_dist_down, man_dist_right, man_dist_left]))

    ## apply move
    if (i == 0): head.direction = "up" if head.direction != "down" else "right"
    elif (i == 1): head.direction = "down" if head.direction != "up" else "left"
    elif (i == 2): head.direction = "right" if head.direction != "left" else "up"
    else: head.direction = "left" if head.direction != "right" else "down"

    # check for collision with food
    if head.distance(food) < 20:
        # move food to random location
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        # add a new_segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # shorten delay
        #delay -= 0.001

        # increase score
        score += 20

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align = "center", font = ("Courier", 24, "normal"))

    # move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x , y)

    move()

    for i in range(1, len(segments), 1):
        if segments[i].distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            # hide the segments
            for j in range(1, len(segments), 1):
                segments[j].goto(1000, 1000)

            segments = [head]
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align = "center", font = ("Courier", 24, "normal"))

            break

    time.sleep(delay) # adding the delay counter to sceen refreshes

wn.mainloop()
