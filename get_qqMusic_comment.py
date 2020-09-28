'''
爬取QQ音乐评论
QQ音乐-周杰伦-等你下课：https://y.qq.com/n/yqq/song/001J5QJL1pRQYB.html
'''

import requests, time

headers = {
      'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}

commentid = ''
# range(), 获取的页数
for pagenum in range(5):
    params = {
        "g_tk_new_20200303":"5381",
        "g_tk":"5381",
        "loginUin":"0",
        "hostUin":"0",
        "format":"json",
        "inCharset":"utf8",
        "outCharset":"GB2312",
        "notice":"0",
        "platform":"yqq.json",
        "needNewCode":"0",
        "cid":"205360772",
        "reqtype":"2",
        "biztype":"1",
        "topid":"212877900",
        "cmd":"8",
        "needmusiccrit":"0",
        "pagenum":pagenum,
        "pagesize":"25",
        "lasthotcommentid":commentid,
        "domain":"qq.com",
        "ct":"24",
        "cv":"10101010"
    }
    res = requests.get('https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg', headers=headers, params=params)
    items = res.json()
    for i in items['comment']['commentlist']:
        # 跳过被删除的评论
        try:
            print('{} : {}'.format(str(i['rootcommentnick']).replace('@', ''), str(i['rootcommentcontent']).replace('\r', '')))
        except Exception:
            continue
    print('\n----------当前页----------' + str(pagenum + 1) + '\n')
    commentid = items['comment']['commentlist'][-1]['commentid']
    time.sleep(2)
