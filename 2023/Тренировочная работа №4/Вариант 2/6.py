from turtle import *
s=30
lt(90)
tracer(False)
x=4
for i in range(4):
    fd(x*s)
    rt(90)
    fd(x*s)
    lt(90)
    fd(x*s)
    rt(90)
up()
for x in range(-5,20):
    for y in range(-5,20):
        goto(x*s,y*s)
        dot(5)
done()
for x in range(2,100):
    if 5*(x-1)**2+4*(x-1)>1500:
        print(x)
        break