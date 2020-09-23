import os
import pandas
import tushare as ts

csv_file = './data.csv'
if not os.path.exists(csv_file):
    pro = ts.pro_api('f3d199a689c5412c7d9569483500a6c17238333e0fc5a6f214938f55')
    data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,market,symbol,name,area,industry,list_date')
    data.to_json('./data.json')
    data.to_csv('./data.csv')
else:
    data = pandas.read_csv(csv_file)

# 所有A股上市公司统计
data_a = data.groupby('area').size().reset_index(name='count').sort_values(by='count', ascending=False)
data_a.to_csv('statistic_a.csv')
print(data_a)


# 科创板数据统计
data_tech = data[data['market']=='科创板']
# print(data)
data_tech = data_tech.groupby('area').size().reset_index(name='count')
data_tech = data_tech.sort_values(by='count', ascending=False)
data_tech.to_csv('statistic_tech.csv')
print(data_tech)