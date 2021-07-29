#iterable 可疊代資料
#字串，列表，集合，字典

#for 變數名稱 in 可疊代資料
dic={'a':3,'b':4}
for key in dic:
    print(key)
    print(dic[key])   #印出字典內的資料


#內建函式
#max()
ans=max([10,20,30])
print(ans)

x=max('afy')
print(x)
#sorted()
y=sorted('cba')   #由小到大 a-b-c
print(y)

o=sorted({10,-9,80,100})
print(o)