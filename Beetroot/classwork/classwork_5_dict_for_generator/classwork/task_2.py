from collections import defaultdict

desk_len = 8
keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
chest = defaultdict(list)
for pos, key in enumerate(keys):
    if pos % 2 == 0:
        for i in range(desk_len):
            if i % 2 == 0:
                chest[key].append('black')
            else:
                chest[key].append('white')
    else:
        for i in range(desk_len):
            if i % 2 == 0:
                chest[key].append('white')
            else:
                chest[key].append('black')

position = input('Введіть позицію шахової фігури: ')
print(chest[position[0]][int(position[1]) - 1])
