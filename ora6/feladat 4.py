input_values = []
while len(input_values) == 0 or input_values(len(input_values) - 1) != (""):
    input_values.append(input())
input_values.remove("")
print(input_values)