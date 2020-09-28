import requests
from bs4 import BeautifulSoup

headers = {
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}

# 获取网页源代码
res = requests.get('https://book.douban.com/top250', headers=headers)
# 转换成BeautifulSoup对象
soup = BeautifulSoup(res.text, 'html.parser')

a = soup.select('div.pl2 a')    #CSS子元素选择
for i in a:
    text = i['title']   # 返回书籍标题
    link = i['href']    # 返回书籍链接
    print(text + " " + link)