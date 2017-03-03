import turtle

def drawSquare(some_turtle):

    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)
        
def drawCircle(some_turtle):

    for i in range(1,5):
        some_turtle.shape("circle")
        

    
def drawArt():

    window = turtle.Screen()
    window.bgcolor("black")


    sudeep = turtle.Turtle()
    sudeep.color("red")
    sudeep.shape("turtle")
    sudeep.speed(2)

    for i in range(1,5):
        drawSquare(sudeep)
        sudeep.right(10)


    narkar = turtle.Turtle()
    narkar.color("blue")
    narkar.shape("turtle")
    narkar.speed(2)

    for i in range(1,10):
        drawCircle(narkar)
        sudeep.right(10)

       
    window.exitonclick()

drawArt()    
