from selenium import webdriver
from bs4 import BeautifulSoup
import time

# 初始化配置
# options = webdriver.ChromeOptions()
# # headless 为静默模式,不打开浏览器节省资源
# options.add_argument('--headless')
# 打开浏览器
# browser = webdriver.Chrome(options=options)

browser = webdriver.Chrome()
browser.get('https://wpblog.x0y1.com/')
# with open('pa.html', 'w', encoding='utf-8') as f:
#     f.write(browser.page_source)

# 查找h1标签
# h1 = browser.find_element_by_tag_name('h1')
# print(h1.text)

# link = browser.find_element_by_link_text('扇贝编程')
# <a href="https://wpblog.x0y1.com/" rel="home">扇贝编程</a>
# print(link.get_attribute('href'))
# print(link.text)

# 用BeautifulSoup解析网页源代码
# soup = BeautifulSoup(browser.page_source, 'html.parser')
# a_all = soup.find_all('a')
# for tag in a_all:
#     print(tag.text)

# class_name = browser.find_element_by_class_name('more-link')
# print(class_name.get_attribute('href'))

search = browser.find_element_by_class_name('search-field')
search.send_keys('python')
time.sleep(1)
search_sub = browser.find_element_by_class_name('search-submit')
search_sub.click()

time.sleep(1)
titles = browser.find_elements_by_class_name('entry-title')
for i in titles:
    print(i.text)

# 2秒加载网页
time.sleep(2)
# 关闭浏览器
browser.quit()