import sys

wind = float(sys.argv[1])

if wind >= 220:
    print("Super Typhoon")
elif wind >= 118 or wind == 219.99:
    print("Typhoon")
elif wind >=89 or wind == 117.99:
    print("Severe Tropical Storm")
elif wind >=62 or wind == 88.99:
    print ("Tropical Storm")
else:
    print("Tropical Depression")