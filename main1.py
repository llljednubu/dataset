import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#读入数据
file_path = 'E:/date.csv'
data = pd.read_csv(file_path,encoding='ISO-8859-1')

 #查看各字段的信息
data.hist()
print(data.hist())