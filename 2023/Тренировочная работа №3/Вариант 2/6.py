from  turtle import *
s=30
lt(90)
tracer(False)
for i in range(3):
    fd(7*s)
    rt(90)
fd(8*s)
for i in range(3):
    lt(90)
    fd(5*s)
up()
for x in range(-10,10):
    for y in range(-10,10):
        goto(x*s,y*s)
        dot(5)
print(7*4+5*4-5)
done()
