# Write a script that creates a new output file called myfile.txt
# and writes the string "Hello file world!" in it

file1_path = 'myfile.txt'
file2_path = 'D:/Python/Beetroot/homework/homework_10_working_with_files/myfile.txt'
file3_path = 'D:/Python/Beetroot/homework/homework_10_working_with_files/files/myfile.txt'
files_path = {file1_path: ' ', file2_path: ' another ', file3_path: ' different '}

for f_path in files_path:
    with open(f_path, 'w') as f:
        f.write(f'Hello,{files_path[f_path]}file world!\n')


