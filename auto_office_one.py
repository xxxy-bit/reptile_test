'''
表格汇总
'''


import openpyxl, csv, os

# with open('12月销售数据汇总.csv', 'w', newline='') as file:
#     csv_write = csv.writer(file)
#     with open('2019-12-01-销售数据.csv', newline='') as file:
#         csv_read = csv.reader(file)
#         csv_write.writerows(csv_read)

csv_path = os.path.abspath(r'.\csvfiles')
msg = [
    ['日期', '来源', '访客数', '买家数', '交易额'],
    ['2019-12-01', '来源01', '837', '23', '1253'],
    ['2019-12-01', '来源02', '493', '32', '968'],
    ['2019-12-01', '来源03', '2285', '591', '12482'],
    ['2019-12-01', '来源04', '119', '17', '1433'],
    ['2019-12-01', '来源05', '12', '0', '0'],
    ['2019-12-01', '来源06', '254', '9', '734'],
    ['2019-12-01', '来源07', '23', '0', '0'],
    ['2019-12-01', '来源08', '133', '2', '234'],
    ['2019-12-01', '来源09', '647', '1', '68'],
    ['2019-12-01', '来源10', '6', '3', '236']
]

# 创建销售数据文件(1-30)
filename = ['2019-12-%02d-销售数据.csv' %(i + 1) for i in range(31)]
# for i in filename:
#     with open(csv_path + '\\' + i, 'w', newline='') as file:
#         csv_msg = csv.writer(file)
#         csv_msg.writerows(msg)

# 汇总12月销售数据
with open('12月销售数据汇总.csv', 'w', newline='') as file:
    csv_12sum = csv.writer(file)
    for i in filename:
        with open(csv_path + '\\' + i, newline='') as file:
            csv_msg = csv.reader(file)
            # 只保留第一个文件的表头，去掉其他文件表头，否则会造成表头重复
            if i == filename[0]:
                rows = csv_msg
            else:
                rows = list(csv_msg)[1:]
            csv_12sum.writerows(rows)