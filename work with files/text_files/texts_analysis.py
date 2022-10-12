from word_count import count_words

filenames = ['Alice in Wonderland.txt', 'Moby Dick.txt', 'Віка.txt', 'Siddhartha.txt']

print()
for filename in filenames:
    file_path = f"C:/Users/admin/Desktop/For files/{filename}"
    count_words(filename, file_path)
print()
