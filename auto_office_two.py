import csv

with open('12月销售计算数据汇总.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    with open('12月销售数据汇总.csv', newline='') as file:
        csv_reader = csv.reader(file)
        for index, row in enumerate(csv_reader):
            if index == 0:  # 第一个表头
                csv_writer.writerow(row + ['购买转化率', '客单价']) #添加两个新表头
            else:
                visitors = int(row[2])  # 访客数
                buyers = int(row[3])    # 买家数
                gmv = int(row[4])       #交易额
                sale_rate = buyers / visitors if visitors else 0    # 购买转化率
                pct = gmv / buyers if buyers else 0                 # 客单价
                csv_writer.writerow(row + [sale_rate, pct])         # 添加购买转化率和客单价