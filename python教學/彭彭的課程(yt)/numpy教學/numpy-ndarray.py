import numpy as np
#建立一維陣列
data=np.array([3,21,45,3])
print(data)
data=np.empty(4)
print(data)
data=np.zeros(3)
print(data)
data=np.ones(3)
print(data)
#建立二維陣列
data=np.array([    #3X3的二維陣列
    [3,2,5],
    [36,56,12],
    [25,21,54]

])
print(data)
data=np.empty([5,5])   #5x5的二維陣列，資料未定
print(data)
data=np.ones([3,2])    #3x2的二維陣列，資料都是1
print(data)

#建立三維陣列
data=np.array([       #2x2x2的三維陣列
[
    [3,1],[5,4]
],
[
    [8,9],[7,3]
]

])
print(data)

data=np.empty([3,2,1])   #3x2x1的陣列
print(data)


#建立多維陣列
data=np.array([       #1x1x2x3的四維陣列
[
[
[3,1,2],[5,4,6]
]
]

])

print(data)

data=np.ones([3,2,1,2])  #3x2x1x2的四維陣列，資料都是1
print(data)