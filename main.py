from turtle import Turtle, Screen
import random
### TURTLES ###
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
turtles = []    # Access turtles using indexing 0-7
y_positions = [150, 100, 50, 0, -50, -100, -150]
for turtle_index in range(0, 7):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    new_turtle.color(colors[turtle_index])
    turtles.append(new_turtle)

### GUI ####
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet!", prompt='Which turtle will win the race? Enter a color: ').lower()

### GAME VARIABLES ###
is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:                              # Loops through all the turtle indexes
        if turtle.xcor() > 230:                         # 230 is the finish line, every iteration it will check
            winner = (turtle.pencolor())                    # prints the color of the winning turtle
            is_race_on = False
            if user_bet == winner:
                screen.textinput('END OF RACE', f"{winner} finished first, You win!")
            else:
                screen.textinput('END OF RACE', f"{winner} won the race! You loose!")
        random_distance = random.randint(0, 10)         # Each turtle will calculate a random distance
        turtle.forward(random_distance)                 # ONE TURTLE AT A TIME









screen.listen()
screen.exitonclick()
