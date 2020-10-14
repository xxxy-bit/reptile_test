'''

授权码：在QQ邮箱设置→账号中查找
SMTP服务器地址：smtp.qq.com

'''

import yagmail

user='785815707@qq.com'     # 发送人的邮箱
password='XXXXXX' # 发送人的授权码
host='smtp.qq.com'          # 发送人的SMTP服务器地址
yag = yagmail.SMTP(user=user, password=password, host=host)

# yag.send(to=['785815707@qq.com'], subject='python 自动发送邮件', contents='hello Python，请多多指教。')

# 发送信息，contents可以是文件路径或者纯文字，如果文件路径没有该文件，则当作文字发送
yag.send(to=['785815707@qq.com'], subject='python 自动发送邮件', contents=['这是12月份的销售数据汇总表，请查收~', r'G:\vsWork\pa\12月销售计算数据汇总.csv'])