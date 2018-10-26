print(bin(4))
print(hex(10))
print(max([1,2,3,4,5]))
print(sum([1,2,3,4,5]))
print(sorted([1,4,3,5,2]))
print()

def square(x):
    return x * x

x = 10
print("{}**2 == {}".format(x, square(x)))
print()

for y in range(10):
    print("{}**2 == {}".format(y, square(y)))