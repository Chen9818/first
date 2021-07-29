import numpy as np
#逐元運算(elementwise)
data1=np.array([3,21,2])
data2=np.array([4,2,2])
p=data1+data2
print(p)

o=data1>data2
print(o)

print('====================')
#矩陣運算(matrix)
data1=np.array([
    [3,2]
])  #1x2

data2=np.array([
    [2,5,1],
    [2,1,2]
])     #2x3

r=data1@data2
print(r)        #內積  1x3

g=np.outer(data1,data2)
print(g)         #外積   2x6
print('==========================')
#統計運算(statistics)
data=np.array([
    [2,1,7],
    [-5,3,8]
])

t=data.sum()
print(t)


t=data.sum(axis=0)  #針對欄做總和column(針對第一個維度做總和
print(t)

t=data.sum(axis=1)  #針對列做總和row(針對第二個維度做總和
print(t)

m=data.max(axis=0)
print(m)

t=data.mean(axis=1)
print(t)

e=data.cumsum()   #逐值累加
print(e)

e=data.cumsum(axis=0)   #逐值累加針對欄
print(e)