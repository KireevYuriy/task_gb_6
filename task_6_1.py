import requests

url = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
response_get = requests.get(url)
with open('nginx_logs.txt', 'w+', encoding='utf-8') as f:
    f.writelines(response_get.content.decode('utf-8'))

array_tuple = []

with open('nginx_logs.txt', 'r', encoding='UTF-8') as f:
    line_f = f.readline().strip()
    while line_f:
        string = line_f.split(' ')
        array = (string[0], string[5][1:], string[6])
        array_tuple.append(array)
        line_f = f.readline().strip()
print(array_tuple)




