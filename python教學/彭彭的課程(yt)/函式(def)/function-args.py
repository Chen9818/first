#參數的預設資料
def mm(b1,b2=0):     #0是預設資料，若b2沒有輸入資料就帶入0
    print(b1**b2)

mm(3,2)
mm(4)

#使用參數名稱對應
def gg(n1,n2):
    print(n1//n2)
gg(5,4)
gg(n2=8,n1=17)


#無限參數資料
def oo(*z):         #*代表可以放入無限多資料
    sum=0
    for n in z :
        sum=sum+n
    print(sum/len(z))
oo(2,5) 
oo(332,22)



