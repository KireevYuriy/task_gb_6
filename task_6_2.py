dict_ip = {}

with open('nginx_logs.txt', 'r', encoding='UTF-8') as f:
    line_f = f.readline().strip()
    while line_f:
        string = line_f.split(' ')
        dict_ip.setdefault(string[0], 1)
        dict_ip[string[0]] += 1
        line_f = f.readline().strip()
spam = max(dict_ip.values())
print('ip-address:', *(key for key, val in dict_ip.items() if val == spam), '\nsize of spam:', spam)
