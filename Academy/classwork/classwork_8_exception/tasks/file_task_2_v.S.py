def main():
    with open('is_even.txt', 'w') as file:
        while True:
            a = get_int()
            if a:
                b = is_even(a)
                print(a, b, file=file)


def get_int():
    num = input("Please, enter a number: ")
    try:
        return int(num)
    except ValueError:
        print("It's not a number!")
    else:
        return False


def is_even(n):
    if n % 2 == 0:
        return 'is even'
    return 'is odd'


if __name__ == "__main__":
    main()