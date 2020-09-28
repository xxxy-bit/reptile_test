'''
爬取豆瓣书籍前250
'''

import requests, time
from bs4 import BeautifulSoup

def select_book(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    a = soup.find_all('div', class_='pl2')
    lis = []
    for i in a:
        tag = i.find('a')   # 遍历a标签
        text = tag['title'] # 返回标签的文本信息
        link = tag['href']  # 返回标签的其他元素
        lis.append(text + " : " + link)
    return lis

if __name__ == "__main__":
    url = 'https://book.douban.com/top250?start={}'
    urls = [url.format(i*25) for i in range(10)]

    for i in urls:
        print(select_book(i))
        print()
        # 暂停2秒，防止访问太快被封
        time.sleep(2)