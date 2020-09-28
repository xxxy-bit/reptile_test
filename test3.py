import requests
from bs4 import BeautifulSoup

headers = {
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}

res = requests.get('https://book.douban.com/top250', headers = headers)

# 第一个参数为网页源码，第二个参数为解析器
soup = BeautifulSoup(res.text, 'html.parser')

print(soup.find('span', class_='inq'))     #返回符合条件的首个数据
print(soup.find_all('span', class_='inq'))     #返回符合条件的首个数据

# print(type(soup))

# print(soup.find_all('class')) #返回符合条件的全部数据