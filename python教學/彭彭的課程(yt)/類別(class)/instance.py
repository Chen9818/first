





#point實體物件的設計:平面座標上的點 
class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
#建立第一個實體物件
p1=point(3,4)
print(p1.x,p1.y)      
#建立第二個實體物件
p2=point(5,6)
print(p2.x,p2.y)



#fullname 實體物件設計:分開紀錄性、明資料的全名
class fullname:
    def __init__(self,first,last):
        self.first=first
        self.last=last
name1=fullname('wei','zhung')
print(name1.first,name1.last)
name2=fullname('pop','guy')
print(name2.first,name2.last)






