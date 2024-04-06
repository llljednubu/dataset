#本段代码实现图标的直方图散点图与箱型图
import pandas as pd	#文件读取
import matplotlib.pyplot as plt #绘图


#寻找最大最小值与均值
score = pd.read_csv('E:/date.csv',encoding = 'gbk')
#最大值
Al_Max = score.Al.max()
Co_Max = score.Co.max()
Cr_Max = score.Cr.max()
Cu_Max = score.Cu.max()
Fe_Max = score.Fe.max()
Ni_Max = score.Ni.max()
#最小值
Al_Min = score.Al.min()
Co_Min = score.Co.min()
Cr_Min = score.Cr.min()
Cu_Min = score.Cu.min()
Fe_Min = score.Fe.min()
Ni_Min = score.Ni.min()
#方差
Al_Var = score.Al.var()
Co_Var = score.Co.var()
Cr_Var = score.Cr.var()
Cu_Var = score.Cu.var()
Fe_Var = score.Fe.var()
Ni_Var = score.Ni.var()
#均值
Al_Avg = score.Al.mean()
Co_Avg = score.Co.mean()
Cr_Avg = score.Cr.mean()
Cu_Avg = score.Cu.mean()
Fe_Avg = score.Fe.mean()
Ni_Avg = score.Ni.mean()

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
total=score.Al+score.Co+score.Cr+score.Cu+score.Fe+score.Ni
p1=plt.figure()#创建画布
a1=p1.add_subplot(2,2,1)#绘制第一幅子图

#直方图
plt.title('元素分布直方图')
plt.xlabel('Num')
plt.ylabel('rate')
plt.bar(score.Num,score.Al)
plt.show()
plt.bar(score.Num,score.Co)
plt.show()
plt.bar(score.Num,score.Cr)
plt.show()
plt.bar(score.Num,score.Cu)
plt.show()
plt.bar(score.Num,score.Fe)
plt.show()
plt.bar(score.Num,score.Ni)
plt.show()

#散点图
plt.title('元素分布散点图')
plt.xlabel('Num')
plt.ylabel('rate')
plt.scatter(score.Num,score.Al)
plt.show()
#其他元素类似

#箱型图
plt.title('元素箱线图')
plt.xlabel('rate')
plt.ylabel('Num')
label = ['Al','Co','Cr','Cu','Fe','Ni']
s = (score.Al,score.Co,score.Cr,score.Cu,score.Fe,score.Ni)
plt.boxplot(s,labels = label)
plt.show()
