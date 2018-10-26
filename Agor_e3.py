number_input=input("Enter a comma separated list of numbers: ")
user_input = number_input.split(",")

accumulator=0
index=0

for x in user_input:
    accumulator += float(user_input[index])**2
    index += 1

print("Sum of squares:", accumulator)
    