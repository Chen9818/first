#定義類別，與類別屬性(封裝在類別中的變數和函式)
#定義一個類別IO，有兩個屬性supportedsrcs和read


class io:
    supportedsrcs=['console','file']
    def read(src):
        if src not in io.supportedsrcs:
            print('not supported')
        else:
            print('read from',src)

    

#使用類別
print(io.supportedsrcs)
io.read('file')
io.read('internet')
