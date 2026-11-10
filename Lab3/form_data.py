from random import randint

names = ["Алиса", "Степан", "Данил", "Миша", "Никита", "Артём", "Дима", "Андрей"]
dct = dict()

for name in names:
    dct[name] = [randint(2, 5) for _ in range(randint(7, 12))]

print(dct)