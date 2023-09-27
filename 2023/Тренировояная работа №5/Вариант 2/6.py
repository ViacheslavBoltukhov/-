from turtle import *
s=30
tracer(False)
x=1
for i in range(6):
    fd(x*s)
    rt(90)
    fd(7*s)
up()
for x in range(-20,20):
    for y in range(-20,20):
        goto(x*s,y*s)
        dot(5)
while (x+8)**2<=900:
    x+=1
print(x)