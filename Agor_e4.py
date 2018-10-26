import geometry

userinput= input("Enter the side lengths of a triangle: ")
inputted= userinput.split(",")

(a,b,c)= (float(number) for number in inputted)

P=geometry.triangle_perimeter(a,b,c)
A=geometry.triangle_heronsarea(a,b,c)

print("Perimeter: {:.4f}".format(P))
print("Area: {:.4f}".format(A))