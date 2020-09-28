'''
爬取豆瓣电影前250
'''

import requests, time
from bs4 import BeautifulSoup

def select_movie(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    lis = []
    items = soup.select('div.hd a')
    for i in items:
        text = i.find('span', class_='title').text
        link = i['href']
        lis.append(text + " : " + link)
    return lis

if __name__ == "__main__":
    url = 'https://movie.douban.com/top250?start={}&filter='
    urls = [url.format(i*25) for i in range(10)]

    for i in urls:
        print(select_movie(i))
        print()
        # 暂停2秒，防止访问太快被封
        time.sleep(2)