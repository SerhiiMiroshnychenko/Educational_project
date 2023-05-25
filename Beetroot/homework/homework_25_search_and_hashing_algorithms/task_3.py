# Реалізувати in (__contains__) та len (__len__) методи для HashTable

class HashTable:
    def __init__(self, size=15):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hash_value = self.hash_function(key, self.size)

        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        elif self.slots[hash_value] == key:
            self.data[hash_value] = data
        else:
            next_slot = self.re_hash(hash_value, len(self.slots))
            while self.slots[next_slot] is not None and self.slots[next_slot] != key:
                next_slot = self.re_hash(next_slot, len(self.slots))

            if self.slots[next_slot] is None:
                self.slots[next_slot] = key
            self.data[next_slot] = data

    @staticmethod
    def hash_function(key, size):
        return key % size

    @staticmethod
    def re_hash(old_hash, size):
        return (old_hash + 1) % size

    def get(self, key):
        start_slot = self.hash_function(key, self.size)

        data = None
        stop = False
        found = False
        position = start_slot
        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.re_hash(position, self.size)
                if position == start_slot:
                    stop = True

        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def __contains__(self, item):
        return any(value == item for value in self.data)

    def __len__(self):
        return sum(slot is not None for slot in self.slots)



if __name__ == "__main__":
    H = HashTable()
    H[54] = "cat"
    H[26] = "dog"
    H[93] = "lion"
    H[17] = "tiger"
    H[77] = "bird"
    H[31] = "cow"
    H[44] = "goat"
    H[55] = "pig"
    H[20] = "chicken"
    H[88] = 'frog'
    H[48] = 'alien'
    print(H.slots)
    print(H.data)

    print(H[20])

    print(H[17])
    H[20] = "duck"
    print(H[20])
    print(H[99])

    print('pig' in H)
    print('elephant' in H)
    print(len(H))
