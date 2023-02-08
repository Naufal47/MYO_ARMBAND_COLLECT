
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# datamyo1 = pd.read_csv("myothreadbareng.csv").drop(['Unnamed: 0'],axis=1)
# datamyo2 = pd.read_csv("threadmyo2.csv").drop(['Unnamed: 0'],axis=1)
# datamyo3 = pd.read_csv("threadmyo3.csv").drop(['Unnamed: 0'],axis=1)
# datamyo4 = pd.read_csv("threadmyo4.csv").drop(['Unnamed: 0'],axis=1)
# datamyo5 = pd.read_csv("threadmyo5.csv").drop(['Unnamed: 0'],axis=1)
#print(datamyo)
# plt.plot(datamyo.iloc[:,7]);
#plt.plot(datamyo)
# data = pd.concat([datamyo1, datamyo2, datamyo3, datamyo4, datamyo5])
datasudut = pd.read_csv('a_sudut6.csv')
datasudut1 = pd.DataFrame(np.array(datasudut['0'].str.split(',',expand=True)))
plt.plot(datasudut1[1])
plt.show()
# datasudut1.to_csv('a_sudut66.csv')

