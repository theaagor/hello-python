import math

def area_circle(radius):
    return math.pi * radius ** 2

if __name__=="__main__":
    data = input("Enter your radius of a circle: ")
    radius=float(data)

    print("Area of the circle: {:.4f}" .format(area_circle(radius)))