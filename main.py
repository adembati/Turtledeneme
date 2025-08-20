import turtle
drawing_board=turtle.Screen()
drawing_board.bgcolor("lightgreen")
drawing_board.setup(width=600, height=600)
drawing_board.title("Python Turtle")
turtle_instance=turtle.Turtle()
for i in range(4):
    turtle_instance.forward(100)
    turtle_instance.left(90)

turtle.done()

