import turtle as t

class Share:
    def __init__(self, x, y, radius=None, color=None):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw_shape(self):
        raise NotImplementedError('Subclass must implement abstract method.')

class Circle(Share):
    def draw_shape(self):
        t.setx(self.x)
        t.sety(self.y)
        t.down()
        t.speed(1)
        t.color(self.color)
        t.begin_fill()
        t.circle(self.radius)
        t.end_fill()
        t.up()

class Square(Share):
    def draw_shape(self):
        t.setx(self.x)
        t.sety(self.y)
        t.down()
        t.speed(1)
        t.color(self.color)
        t.begin_fill()
        t.right(180)
        for _ in range(4):
            t.forward(self.radius * 2)
            t.right(90)
        t.end_fill()
        t.up()

if __name__ == '__main__':
    my_square0 = Square(0, 0, 100, 'blue')
    my_circle0 = Circle(-100, 200, 100, 'yellow')
    my_square1 = Square(-171, 171, 71, 'blue')
    my_circle1 = Circle(-100, 28, 72, 'yellow')
    my_square0.draw_shape()
    my_circle0.draw_shape()
    my_square1.draw_shape()
    my_circle1.draw_shape()
    t.down()
    t.up()


