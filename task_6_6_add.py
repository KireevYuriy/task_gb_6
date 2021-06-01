def add_price(arg):
    with open('bakery.csv', 'a', encoding='UTF-8') as f:
        f.write(f'{arg}\n')



