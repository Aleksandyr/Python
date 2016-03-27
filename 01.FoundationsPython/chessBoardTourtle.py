import turtle
side = 50
deg = 90
x = -300
y = 150
counter = 0

turtle.penup()
turtle.goto(x,y)
turtle.pendown()

for row in range(8):
	for col in range(8):
	    if ((col + counter) % 2) == 0:
	    	turtle.begin_fill()   

	    for rect in range(4):
	    	turtle.forward(side)
	    	turtle.left(deg)	    

	    if ((col + counter) % 2) == 0:
	    	turtle.end_fill()     
	    
	    turtle.forward(side)
	
	y -= 50

	turtle.penup()
	turtle.goto(x,y)
	turtle.pendown()

	counter += 1

turtle.exitonclick()