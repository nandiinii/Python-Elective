import turtle as t
t.circle(100)
t.penup()
t.pensize(4)
t.goto(-30,120)#Left Eye
t.pendown()
t.dot(25)
t.penup()
t.goto(30,120)#Right Eye
t.pendown()
t.dot(25)
t.penup()
t.goto(-30,40)#Mouth
t.pendown()
t.forward(60)
t.penup()
t.goto(0,100)#Nose
t.pendown()
t.goto(0,50)
t.penup()
t.goto(-60,145)#Left EyeBrow
t.pendown()
t.forward(40)
t.penup()
t.goto(20,145)#Right Eyebrow
t.pendown()
t.forward(40)
t.penup()
t.mainloop()