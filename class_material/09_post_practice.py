import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57'
}

url = 'https://www.w3schools.com/action_page.php'


data_str = '''_hid_0: 564328
_hid_1: 352167
_hid_2: 57483
1A: Apple
2A: Dog
cars: volvo
subject1: Car Loan
subject2: zxczxczxc
subject3: asdasdasd'''

data = {row.split(': ')[0]: row.split(': ')[1] for row in data_str.split('\n')} #將字串分割，並寫入字典

#原本迴圈的寫法如下
# data = {}
# for row in data_str.split('\n'):
#     data[row.split(': ')[0]] = row.split(': ')[1]

print(data)
res = requests.post(url, headers=headers, data=data)
print('====================')
print(res.text)