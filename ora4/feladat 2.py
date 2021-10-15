import random
random_numbers = {}
for number in range(10):
    random_numbers.append(random.randint(1, 100))

even_numbers = {}
odd_numbers = {}
for i in range(len(random_numbers)):
    even_numbers.append(random_numbers[i])


