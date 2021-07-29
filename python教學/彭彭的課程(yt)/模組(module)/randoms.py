#隨機模組
import random



#隨機選取
d=random.sample([1,2,3,4,5],  3)
print(d)

#隨機取得亂數
s=random.random()
print(s)

ss=random.uniform(60,100)
print(ss)

gg=random.normalvariate(100,10)     #平均數100 標準差10
print(gg)

#統計模組
import statistics as st
da=st.stdev([1,2,3,4,5,6,10])   #stdev標準差
print(da)