import turtle 
t = turtle.Turtle()
t.pencolor("red")
t.pensize(5)
t.fillcolor("yellow")
t.begin_fill()
for i in range(6):
   t.forward(100) 
   t.right(60)
t.end_fill()
turtle.mainloop()