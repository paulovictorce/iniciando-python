list = [2, 1, 3, 4, 6, 8, 10]
list2 = ["Paulo", "Victor", "Oliveira"]

for number in list:
    if number % 2 == 0:
        print(number)

for name in list2:
    if not name == "Oliveira":
        print(name)