upper, lower = 0, 0
with open("alice_in_wonderland.txt") as f:
    for line in f:
        if line:
            upper += sum(1 for char in line if 65 < ord(char) < 90)
            lower += sum(1 for char in line if 97 < ord(char) < 122)

percent_u = round(upper / ((upper + lower) / 100), 2)
percent_l = round(lower / ((upper + lower) / 100), 2)

print(f'There is a total of {upper} uppercase and {lower} lowercase characters')
print(f'{percent_u}% of uppercase and {percent_l}% of lowercase characters.')