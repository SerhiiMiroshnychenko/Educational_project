class DoublyNode:
    def __init__(self, data):
        self._data = data
        self._next = None
        self._prev = None

    def get_data(self):
        return self._data

    def set_data(self, data):
        self._data = data

    def get_next(self):
        return self._next

    def set_next(self, new_next):
        self._next = new_next

    def get_prev(self):
        return self._next

    def set_prev(self, new_next):
        self._next = new_next
