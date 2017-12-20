cars = {
    'Idea':"Cinza",
    'Gol': 'Prata',
    '320Bmw': 'Vermelha'

}

print(cars)
print(cars.keys())
print(cars.values())

for key, value in cars.items():
    print(key + " = "+value)