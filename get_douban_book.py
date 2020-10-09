'''
爬取豆瓣书籍前250
https://book.douban.com/top250
'''

import requests, time
from bs4 import BeautifulSoup
from openpyxl import Workbook

if __name__ == "__main__":
    url = 'https://book.douban.com/top250?start={}'
    urls = [url.format(i*25) for i in range(10)] 

    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }

    wb = Workbook()
    sheet = wb.active
    sheet.title = '书籍前250'
    sheet.append(['书籍名称', '书籍链接'])

    for url_go in urls:
        res = requests.get(url_go, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')

        a = soup.find_all('div', class_='pl2')
        
        for i in a:
            tag = i.find('a')   # 遍历a标签
            text = tag['title'] # 返回标签的文本信息
            link = tag['href']  # 返回标签的其他元素
            sheet.append([text, link])
            print(text + " : " + link)

        time.sleep(1)

    wb.save('豆瓣书籍前250.xlsx')