#  Определить, какое число в массиве встречается чаще всего.


from random import randint

SIZE = 200
MIN_ITEM = 0
MAX_ITEM = 100

arr = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print('Исходный массив')
print(arr)

res = {el: 0 for el in arr}
for el in arr:
    res[el] += 1
res_col = 0
for num, col in res.items():
    if res_col < col:
        res_col = col
        res_num = num
print(f'Чаще всего встречается число {res_num}')
