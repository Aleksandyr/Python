import turtle
side = 50
x = -300
y = 150
counter = 0

turtle.penup()
turtle.goto(x,y)
turtle.pendown()

for j in range(8):
	for i in range(8):
	    if ((i + counter) % 2) == 0:
	    	turtle.begin_fill()    
	    turtle.forward(side)
	    turtle.left(90)
	    turtle.forward(side)
	    turtle.left(90)
	    turtle.forward(side)
	    turtle.left(90)
	    turtle.forward(side)
	    turtle.left(90)
	    turtle.end_fill()
	    turtle.forward(side)
	
	y -= 50
	turtle.penup()
	turtle.goto(x,y)
	turtle.pendown()
	counter += 1

turtle.exitonclick()