# QQ音乐流行指数榜：https://y.qq.com/n/yqq/toplist/4.html

import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}

params = {
  "-":"getUCGI020636893487567587",
  "g_tk":"5381",
  "sign":"zzalfjqjq6f60429403a9b3ab5fffa09588cc0d0c93838",
  "loginUin":"0",
  "hostUin":"0",
  "format":"json",
  "inCharset":"utf8",
  "outCharset":"utf-8",
  "notice":"0",
  "platform":"yqq.json",
  "needNewCode":"0",
  "data":"{\"detail\":{\"module\":\"musicToplist.ToplistInfoServer\",\"method\":\"GetDetail\",\"param\":{\"topId\":4,\"offset\":0,\"num\":20,\"period\":\"2020-09-28\"}},\"comm\":{\"ct\":24,\"cv\":0}}"
}

res = requests.get('https://u.y.qq.com/cgi-bin/musics.fcg', headers=headers, params=params)
items = res.json()

for i in items['detail']['data']['data']['song']:
    print('{} : {}'.format(i['rank'], i['title']))

# print('{} : {}'.format(items['detail']['data']['data']['song'][0]['rank'], items['detail']['data']['data']['song'][0]['title']))
