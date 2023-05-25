# Write a decorator that takes a list of stop words and replaces
# them with * inside the decorated function
"""
def stop_words(words: list):
    pass
@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"
assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
"""
def stop_words(words: list):
    def stop_words_decor(func):
        from functools import wraps
        @wraps(func)
        def deleter(text):
            result = func(text)
            for word in words:
                result = result.replace(word.lower(), '*')
                result = result.replace(word.upper(), '*')
                result = result.replace(word.capitalize(), '*')
            return result
        return deleter
    return stop_words_decor

if __name__ == "__main__":
    @stop_words(['pepsi', 'BMW'])
    def create_slogan(name: str) -> str:
        return f"{name} drinks pepsi in his brand new BMW!"


    print(f'Працює функція "{create_slogan.__name__}":')
    print(create_slogan("Steve"))
    print(create_slogan("Pepsi's fan"))
    print(create_slogan("Director of the BMW Company"))
