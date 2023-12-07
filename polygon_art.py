import turtle
import random
class polygon:
    def __init__(self,num_sides, size, orientation, location, color, border_size):
        turtle.penup()
        self.locotion = turtle.goto(location[0], location[1])
        self.orientation = turtle.setheading(orientation)
        self.color = turtle.color(color)
        self.border_size = turtle.pensize(border_size)
        turtle.pendown()
        for _ in range(num_sides):
            turtle.forward(size)
            turtle.left(360 / num_sides)
        turtle.penup()
    def new_location(self):
        turtle.penup()
        turtle.forward(size*(1-reduction_ratio)/2)
        turtle.left(90)
        turtle.forward(size*(1-reduction_ratio)/2)
        turtle.right(90)

x = int(input("Enter a number between 1 to 8: "))
turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)

if x == 1:
    for i in range(random.randint(12,20)):
        num_sides = 3# triangle, square, or pentagon
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        border_size = random.randint(1, 10)
        x = polygon(num_sides,size,orientation,location,color,border_size)
        reduction_ratio = 0.618
        x.new_location()
        location[0] = turtle.pos()[0]
        location[1] = turtle.pos()[1]
        size *= reduction_ratio
if x == 2:
    for i in range(random.randint(12,20)):
        num_sides = 4# triangle, square, or pentagon
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        border_size = random.randint(1, 10)
        x = polygon(num_sides,size,orientation,location,color,border_size)
        reduction_ratio = 0.618
        x.new_location()
        location[0] = turtle.pos()[0]
        location[1] = turtle.pos()[1]
        size *= reduction_ratio
if x == 3:
    for i in range(random.randint(12,20)):
        num_sides = 5# triangle, square, or pentagon
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        border_size = random.randint(1, 10)
        x = polygon(num_sides,size,orientation,location,color,border_size)
        reduction_ratio = 0.618
        x.new_location()
        location[0] = turtle.pos()[0]
        location[1] = turtle.pos()[1]
        size *= reduction_ratio
if x == 4:
    for i in range(random.randint(12,20)):
        num_sides = random.randint(3,5)# triangle, square, or pentagon
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        border_size = random.randint(1, 10)
        x = polygon(num_sides,size,orientation,location,color,border_size)
        reduction_ratio = 0.618
        x.new_location()
        location[0] = turtle.pos()[0]
        location[1] = turtle.pos()[1]
        size *= reduction_ratio
if x == 5:
    for i in range(random.randint(12, 20)):
        num_sides = 3  # triangle, square, or pentagon
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        border_size = random.randint(1, 10)
        x = polygon(num_sides, size, orientation, location, color, border_size)
        reduction_ratio = 0.618
        x.new_location()
        location[0] = turtle.pos()[0]
        location[1] = turtle.pos()[1]
        size *= reduction_ratio
        x = polygon(num_sides, size, orientation, location, color, border_size)
        x.new_location()
        location[0] = turtle.pos()[0]
        location[1] = turtle.pos()[1]
        size *= reduction_ratio
        y = polygon(num_sides, size, orientation, location, color, border_size)
if x ==6:
    for i in range(random.randint(12,20)):
        num_sides = 4  # triangle, square, or pentagon
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        border_size = random.randint(1, 10)
        x = polygon(num_sides, size, orientation, location, color, border_size)
        reduction_ratio = 0.618
        x.new_location()
        location[0] = turtle.pos()[0]
        location[1] = turtle.pos()[1]
        size *= reduction_ratio
        x = polygon(num_sides, size, orientation, location, color, border_size)
        x.new_location()
        location[0] = turtle.pos()[0]
        location[1] = turtle.pos()[1]
        size *= reduction_ratio
        y = polygon(num_sides, size, orientation, location, color, border_size)
if x ==7:
    for i in range(random.randint(12,20)):
        num_sides = 5  # triangle, square, or pentagon
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        border_size = random.randint(1, 10)
        x = polygon(num_sides, size, orientation, location, color, border_size)
        reduction_ratio = 0.618
        x.new_location()
        location[0] = turtle.pos()[0]
        location[1] = turtle.pos()[1]
        size *= reduction_ratio
        x = polygon(num_sides, size, orientation, location, color, border_size)
        x.new_location()
        location[0] = turtle.pos()[0]
        location[1] = turtle.pos()[1]
        size *= reduction_ratio
        y = polygon(num_sides, size, orientation, location, color, border_size)
if x ==8:
    for i in range(random.randint(12,20)):
        num_sides = random.randint(3,5)  # triangle, square, or pentagon
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        border_size = random.randint(1, 10)
        x = polygon(num_sides, size, orientation, location, color, border_size)
        reduction_ratio = 0.618
        x.new_location()
        location[0] = turtle.pos()[0]
        location[1] = turtle.pos()[1]
        size *= reduction_ratio
        x = polygon(num_sides, size, orientation, location, color, border_size)
        x.new_location()
        location[0] = turtle.pos()[0]
        location[1] = turtle.pos()[1]
        size *= reduction_ratio
        y = polygon(num_sides, size, orientation, location, color, border_size)

turtle.done()

