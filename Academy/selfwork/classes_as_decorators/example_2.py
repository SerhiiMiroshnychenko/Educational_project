class sandwich_cover:
    def __init__(self, cover):
        self._cover = cover

    def __call__(self, func):
        def wrapper(sandwich_with):
            print(self._cover)
            func(sandwich_with)
            print(self._cover)
        return wrapper

@sandwich_cover('Тост')
@sandwich_cover('Хрін')
def sandwich(sandwich_with):
     print(sandwich_with)

sandwich("Ковбаса")