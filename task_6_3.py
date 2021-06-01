import sys

list_name = []
list_hobby = []
file_dict = {}

with open('users.csv', 'r', encoding='utf-8') as f:
    line = f.readline().strip()
    while line:
        string = line.split(',')
        list_name.append(' '.join(string))
        line = f.readline().strip()
with open('hobby.csv', 'r', encoding='utf-8') as f:
    line = f.readline().strip()
    while line:
        list_hobby.append(line)
        line = f.readline().strip()
error_idx = 0
if len(list_name) >= len(list_hobby):
    for i in range(len(list_name)):
        if i+1 > len(list_hobby):
            list_hobby.append(None)
        file_dict.setdefault(list_name[i], list_hobby[i])
else:
    for i in range(len(list_name)):
        file_dict.setdefault(list_name[i], list_hobby[i])
        error_idx += 1
print(file_dict, '\n')
with open('name_hobby.csv', 'w+', encoding='utf-8') as f:
    for elem in file_dict.items():
        f.write(f'{elem}\n')
    f.seek(0)
    print(f.readlines())
if error_idx > 0:
    sys.exit('Error! В файле users.csv меньше записей чем в файле hobby.csv')
