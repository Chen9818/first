#多維陣列維度/形狀操作
import numpy as np


#觀察資料形狀
data=np.array([
    [1,2,3]
    ,[4,5,6]
])
print(data.shape)

data=np.ones(10)
print(data.shape)
#資料轉置
data=np.array([
    [1,2,3]
    ,[4,5,6]
])

print(data.shape)    #2x3
print(data.T.shape)        #3x2

#扁平化資料
data=np.array([
    [
        [2,1],[3,4]
    ],
    [
        [6,1],[5,4]
    ]
])   #2x2x2
p=data.ravel()
print(p)         #一維陣列

#重塑資料形狀
data=np.array([
    [
        [2,1],[3,4]
    ],
    [
        [6,1],[5,4]
    ]
])   #2x2x2=8

datas=data.reshape(4,2)    #改為4x2陣列  切記資料數要相同
print(datas)



data=np.ones(20).reshape(5,2,2)
print(data)

data=np.arange(9).reshape(3,3)
print(data)
print(data.T)