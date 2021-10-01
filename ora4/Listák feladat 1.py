import random
print("1. Feladat:")
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month = ["Január", "Február", "Március", "Április", "Május", "Június", "Július", "Augusztus", "Szeptember", "Október",
         "November", "December"]
months_and_days = []
for i in range(len(month)):
    months_and_days.append(month[i])
    months_and_days.append(days_in_month[i])
print(months_and_days)
print("2. feladat:")
random_ints = [random.randint(0, 1000000000), 61561, 51515, 5616515, 516512023, 134351]
random_ints.sort(reverse=True)
print(random_ints[0])
