#實體物件的設計
class point:   
    def __init__(self,x,y):       #三組定義
        self.x=x
        self.y=y
    def show(self):
        print(self.x,self.y)
    def distance(self,tx,ty):
        return(((self.x-tx)**2)+((self.y-ty)**2))**0.5
p=point(3,4)
p.show()   #呼叫實體方法/函式
re=p.distance(0,0)  #計算座標(3,4)和座標(0,0)間的距離
print(re)

#file實體物件的設計:包裝檔案讀取的程式
class file:
    def __init__(self,name):
        self.name=name
        self.file=None  #尚未開啟檔案:初期是none
    def open(self):
        self.file=open(self.name,mode="r",encoding="utf-8")
    def read(self):
        return self.file.read()
#讀取第一個檔案
f1=file('data1.txt')
f1.open()                   #可以有無限組檔案，只要套用實體物件就可以快速且方便得出解
data=f1.read()
print(data)
#讀取第二個檔案
f2=file('data2.txt')
f2.open()
da=f2.read()
print(da)

