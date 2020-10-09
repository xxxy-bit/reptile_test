from bs4 import BeautifulSoup
import csv, requests

with open('豆瓣书籍前250.csv', 'w', newline='', encoding='utf-8') as file:
    csv_msg = csv.writer(file)
    header = ['书名', '评分', '链接']
    csv_msg.writerow(header)

    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
    res = requests.get('https://book.douban.com/top250', headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    items = soup.find_all(class_='item')

    for i in items:
        tag = i.find(class_='pl2').find('a')
        rating = i.find(class_='rating_nums').text
        name = tag['title']
        link = tag['href']
        row = [name, rating, link]
        csv_msg.writerow(row)
        print(name, rating, link)