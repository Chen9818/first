w=set()
w={'kk','kk','lol'}     #集合會自動刪除重複元素
print(w)

e=['oo','oo','op']   #列表則不會
print(e)

for num,i in enumerate(w):      #
    print(num,'',i)

nums=[100, 55, 39, 44, 2]
a=nums.sort()
print(a)

a=lambda o,p:o+p
print(a(7,9))


print((lambda x,y:x*y)(2,4))