# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.



res = {}
for i in range(2, 10):
    res[i] = 0

for el in range(2, 100):
    for i in range(2, 10):
        if el % i == 0:
            res[i] += 1

for i, el in res.items():
    print(f'Количество кратных {i} равно {el}')

print('Вариант 2')
res = {}
for i in range(2, 10):
    res[i] = 99 // i
    print(f'Количество кратных {i} равно {res[i]}')