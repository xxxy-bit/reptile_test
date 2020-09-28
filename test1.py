import requests
from bs4 import BeautifulSoup

headers = {
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}

res = requests.get('https://movie.douban.com/top250', headers=headers)

soup = BeautifulSoup(res.text, 'html.parser')

items = soup.select('div.hd a')
for i in items:
    text = i.find('span', class_='title').text
    link = i['href']
    print(text + " " + link)




# find查找
# items = soup.find_all('div', class_='hd')
# for i in items:
#     a = i.find('a')
#     text = a.find('span', class_='title').text
#     print(text)
