import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal
from collections import deque
from sklearn.preprocessing import MinMaxScaler


data_flex=pd.read_csv('a_sudut44.csv')
scaler = MinMaxScaler(feature_range=(0,100), copy=True)

y1 = np.array(data_flex['0']).reshape(-1,1)
y2 = np.array(data_flex['1']).reshape(-1,1)
y3 = np.array(data_flex['2']).reshape(-1,1)
y4 = np.array(data_flex['3']).reshape(-1,1)
y5 = np.array(data_flex['4']).reshape(-1,1)

scaler1 = pd.DataFrame(scaler.fit_transform(y1))
scaler2 = pd.DataFrame(scaler.fit_transform(y2))
scaler3 = pd.DataFrame(scaler.fit_transform(y3))
scaler4 = pd.DataFrame(scaler.fit_transform(y4))
scaler5 = pd.DataFrame(scaler.fit_transform(y5))


data_Grip = pd.concat([scaler1, scaler2, scaler3, scaler4, scaler5],axis=1)
data_Myo=pd.read_csv('a_myo4.csv')
index=[]
a=0

Grip=np.array(data_Grip)
Myo=np.array(data_Myo)

# data_skala = MinMaxScaler(feature_range=(0, 10), copy=True)
# data_skala1 = data_skala.fit_transform(Grip)

n_Grip=len(data_Grip)
n_myo=len(data_Myo)

print(n_myo)
# ---------------------------------------------------------------
downsample1=signal.resample(Grip,14000) 
downsample2=signal.resample(Myo,14000)#resample data flex
n_resm1=len(downsample1)
n_resm2=len(downsample2)

print(n_resm1)
print(n_resm2)

# ----------------------------------------------------------------

dataMyo=deque(maxlen=n_resm2-a)

for i in range(n_resm2):
    dataMyo.append(downsample2[i])
np.array(dataMyo)

for i in range(n_resm1-a,n_resm1):
    index.append(i)
dataGrip=np.delete(downsample1,index, axis=0)

Grip_=pd.DataFrame(dataGrip)
Myo_=pd.DataFrame(dataMyo)

datasheet=pd.concat([Myo_,Grip_], axis=1)
# datasheet.to_csv('dataset_a3.csv',index=False)

plt.plot(datasheet)
plt.show()
# print(dataGrip)