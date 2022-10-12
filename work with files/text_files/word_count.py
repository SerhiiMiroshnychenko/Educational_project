def count_words(filename, file_path):
    """Порахувати приблизну кількість слів у файлі"""
    try:
        with open(file_path, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, there is not the file {filename} by address {file_path}.")
    else:
        words = contents.split()
        num_words = len(words)  # порахувати приблизну кількість слів у файлі
        print(f"The file {filename} has about {num_words} words.")