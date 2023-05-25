
def main():
    upper = 0
    lower = 0
    with open("result.txt", 'r') as file:
        for line in file:
            if line:
                upper += sum(1 for c in line if c.isupper())
                lower += sum(1 for c in line if c.islower())

    percent_u = round(upper / ((upper + lower) / 100), 2)
    percent_l = round(lower / ((upper + lower) / 100), 2)

    print(f'There is a total of {upper} uppercase and {lower} lowercase characters')
    print(f'{percent_u}% of uppercase and {percent_l}% of lowercase characters.')


if __name__ == "__main__":
    main()

