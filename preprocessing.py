#本段代码找出数据的缺失值与异常值并进行数目标注
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#读入数据
file_path = 'E:/date.csv'
data = pd.read_csv(file_path,encoding='ISO-8859-1')

data.info() #查看各字段的信息
print(data.isnull().sum())  #统计每列有几个缺失值
missing_col = data.columns[data.isnull().any()].tolist() #找出存在缺失值的列


import numpy as np
#统计每个变量的缺失值占比
def CountNA(data):
    cols = data.columns.tolist()    #cols为data的所有列名
    n_df = data.shape[0]    #n_df为数据的行数
    for col in cols:
        missing = np.count_nonzero(data[col].isnull().values)  #col列中存在的缺失值个数
        mis_perc = float(missing) / n_df * 100
        print("{col}的缺失比例是{miss}%".format(col=col,miss=mis_perc))

    #data.dropna(axis=0, how="any", inplace=True)  # axis=0代表'行','any'代表任何空值行,若是'all'则代表所有值都为空时，才删除该行
    #data.dropna(axis=0, inplace=True)  # 删除带有空值的行
    #data.dropna(axis=1, inplace=True)  # 删除带有空值的列

#找出异常值并确定占比
neg_list = ['Al','Co','Cr','Cu','Fe','Ni']
for item in neg_list:
    neg_item = data[item] < 10
    print(item + '小于10的有' + str(neg_item.sum())+'个')

#删除小于10的记录
for item in neg_list:
    data = data[(data[item]>=10)]


