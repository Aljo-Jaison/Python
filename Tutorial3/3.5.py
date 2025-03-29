import turtle

def radhexagon(size):
    for _ in range(6):
        turtle.forward(size)
        turtle.right(60)

def radial_pattern(len, count):
    for _ in range(count):
        radhexagon(len)
        turtle.right(360 / count)

turtle.speed(0.5)
radial_pattern(50, 10)

turtle.done()

