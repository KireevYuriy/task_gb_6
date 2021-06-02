
def add_price(arg):

    with open('bakery.csv', 'a', encoding='UTF-8') as f:
        f.write(f'{arg}\n')


def show_price(interval):

    start = 1 if len(interval) == 1 else int(interval[1])
    step = 0 if len(interval) < 3 else int(interval[2])
    with open('bakery.csv', 'r', encoding='UTF-8') as f:
        file_lines = f.readline().strip()
        i = 1
        while file_lines:
            if i != step:
                if i >= start:
                    print(file_lines)
                    file_lines = f.readline().strip()
                else:
                    file_lines = f.readline().strip()
            else:
                break
            i += 1


def edit_price(arg):

    idx = arg[1]
    value = arg[2] + '\n'
    with open('bakery.csv', 'r+', encoding='UTF-8') as f:
        file_lines = f.readline().strip()
        i = 1
        while file_lines:
            if i == int(idx):

                file_lines = file_lines.replace(file_lines, value)
                f.seek(0)
                f.writelines(file_lines)
            file_lines = f.readline().strip()
            i += 1

