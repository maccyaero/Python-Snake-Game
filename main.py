from turtle import Screen, Turtle

SnakeColor = "white"
SnakeShape = "square"
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
list_of_turtles = []

turtle1 = Turtle(SnakeShape)
turtle1.color(SnakeColor)
list_of_turtles.append(turtle1)


def create_new_turtle():
    turtle = Turtle(SnakeShape)
    turtle.color(SnakeColor)
    turtle.setpos(get_position_of_last_block())
    list_of_turtles.append(turtle)


def get_position_of_last_block():
    position = (list_of_turtles[-1].pos()) - (20, 0)
    return position


create_new_turtle()
create_new_turtle()

screen.exitonclick()
