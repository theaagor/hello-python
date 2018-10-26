class Point():
    def __init__(self, a = 0.0, b = 0.0):
        self.x = a
        self.y = b

    def __str__ (self):
        return "({},{})".format(self.x,self.y)

p= Point(3.44,3.65)
print(p)
q = Point(4.8,5.6)
print(q)

