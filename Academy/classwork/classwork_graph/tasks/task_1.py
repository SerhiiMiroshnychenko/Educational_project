def shortest_path(start, goal, dict_):
    from collections import deque

    if start == goal:
        return 0
    if goal not in dict_:
        return 0
    level, wordlength = 0, len(start)

    queue_ =  deque()
    queue_.append(start)
    while len(queue_) > 0:
        level += 1
        size= len(queue_)

        for _ in range(size):
            word = list(queue_.popleft())
            for pos in range(wordlength):
                orig_char = word[pos]
                for c in range(ord('a'), ord('z')+1):
                    word[pos] = chr(c)
                    if "".join(word) == goal:
                        return level + 1
                    if "".join(word) not in dict_:
                        continue
                    del dict_["".join(word)]
                    queue_.append("".join(word))
                word[pos] = orig_char
    return 0


if __name__ == '__main__':

    my_dict = {
        "poon": 1,
        "plee": 1,
        "same": 1,
        "poie": 1,
        "plie": 1,
        "poin": 1,
        "plea": 1,
    }

    print("Length of shortest chain is: ",
          shortest_path('toon', 'plea', my_dict))
