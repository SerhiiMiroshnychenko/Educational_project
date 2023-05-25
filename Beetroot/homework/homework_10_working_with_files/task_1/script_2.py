# Write another script that opens myfile.txt, and reads and prints its contents.

file1path = 'myfile.txt'
file2path = '../myfile.txt'
file3path = '../files_for_task3/myfile.txt'

files_path_ = [file1path, file2path, file3path]

for fpath in files_path_:
    with open(fpath) as f:
        contents = f.read().strip()
    print(f'"{contents}" from: {fpath}')

