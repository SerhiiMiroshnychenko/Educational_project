from pythonds.basic import Deque  # type: ignore


def is_palindrome(word):
    word_deque = Deque()

    for char in word:
        word_deque.addRear(char)

    equal_ = True

    while word_deque.size() > 1 and equal_:
        first = word_deque.removeFront()
        last = word_deque.removeRear()
        if first != last:
            equal_ = False

    return equal_

if __name__ == '__main__':
    print(is_palindrome('abcd'))
    print(is_palindrome('python'))
    print(is_palindrome('madam'))
    print(is_palindrome('racecar'))
