import math

def triangle_perimeter (a, b, c):
    return a + b + c

def triangle_heronsarea (a, b, c):
    s=triangle_perimeter(a,b,c)/2
    area=math.sqrt(s*(s-a))
    
    return area