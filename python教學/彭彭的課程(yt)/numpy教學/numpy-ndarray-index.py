import numpy as np
#多維陣列的索引 indexing
#單維資料
# data=np.array([3,21,2,1])
# print(data[2])

#多維資料
# data=np.array([
#     [1,2,1]
#     ,[5,4,6]
#     ,[8,9,4]
# ])

# print(data[1,2])

#多維陣列的切片 slicing
#單維度資料
# data=np.array([3,21,2,1])
# print(data[0:3])   #[3,21,2]

# print(data[:2])      #[3,21]
# print(data[1:])      #[21,2,1]

#多維度資料
# data=np.array([
#     [14,56,21],[12,11,31]
#     ,[5,4,6],[1,2,3]
# ])
# print(data[1:3,0:2])    #[[12,11],[5,4]]
# print(data[0:2,1])      #[56,11]

#使用...代表全都要

data=np.array([
    [
        [0,1,2],[4,5,6]
    ],
    [
        [12,14,15],[61,21,36]
    ]
])

print(data[0,...])   #[[0,1,2],[4,5,6]]
print(data[...,1:3])  #[[[1,2],[5,6]],[[14,15],[21,36]]]



