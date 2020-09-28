import requests
from bs4 import BeautifulSoup

headers = {
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}

res = requests.get('https://book.douban.com/top250', headers = headers)

soup = BeautifulSoup(res.text, 'html.parser')

a = soup.find_all('div', class_='pl2')
for i in a:
    tag = i.find('a')   # 遍历a标签
    text = ''.join(tag.text.strip())     # 返回标签的文本信息
    link = tag['href']  # 返回标签的其他元素
    print(text)

# print(a)