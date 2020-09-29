'''
Session 在多个请求之间可以共享cookie

loger:codetime
pwd:shanbay520
'''

import requests

session = requests.Session()
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}
data = {
    'log': 'codetime',
    'pwd': 'shanbay520',
    'wp-submit': '登录',
    'redirect_to': 'https://wpblog.x0y1.com',
    'testcookie': '1'
}

comment = {
    'comment': '嗯哼',
    'submit': '发表评论',
    'comment_post_ID': 43,
    'comment_parent': 0
}

session.headers.update(headers)
res = session.post('https://wpblog.x0y1.com/wp-login.php', data=data)
comm = session.post('https://wpblog.x0y1.com/wp-comments-post.php', data=comment)

print(comm.status_code)