import turtle
t=turtle.Turtle()
t.shape("turtle")
points=[[10,-80],[200,-80], [100, 100]]
def draw_polygon(points):
    t.penup()
    t.goto(points[0])
    t.pendown()
    for point in points:
        t.goto(point)
    t.goto(points[0])  
draw_polygon(points)
turtle.mainloop()