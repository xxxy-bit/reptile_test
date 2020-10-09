# 导入CSV库
import csv

# 写入CSV
with open('测试CSV.csv', 'w', newline='') as file:
    # 赋值给csv_msg， 那么这个变量就等于CSV文件，后面操作这个变量即可
    csv_msg = csv.writer(file)
    rows = [
        ['姓名', '出勤天数', '迟到次数'],
        ['小贝', 20, 5],
        ['闻闻', 22, 0]
    ]
    # 逐行写入
    for i in rows:
        csv_msg.writerow(i)

    # 多行写入
    # csv_msg.writerows(rows)

# 读取CSV
# newline='' 是为了让文件内容中的换行符能被正确解析，建议在用 csv 处理文件时都加上这个参数
with open('测试csv.csv', newline='') as file:
    csv_reader = csv.reader(file)   # 读取CSV文件
    for row in csv_reader:
        print(row)