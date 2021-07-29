



#儲存檔案
#第一種寫法
# ll=open('data.txt',mode='w',encoding='utf-8')      #w指寫入模式# encoding='utf-8'可以打入中文
# ll.write("中文測試")
# ll.close


# #第二種寫法(建議)
# with open('data.txt',mode='w',encoding='utf-8') as file:  #file是變數,檔案物件
#     file.write('2\n8')     #以檔案物件寫入檔案



#讀取檔案
# with open('data.txt',mode='r',encoding='utf-8') as file:
#     p=file.read()
# print(p)


#把檔案的數字資料一行行讀取出，並總合
# sum=0
# with open('data.txt',mode='r',encoding='utf-8') as file:
#     for ll in file:       #一行行讀取
#         sum+=int(ll)

# print(sum)


#使用JSON格式讀取，複寫檔案
import json
with open('config.json',mode='r') as file:
    data=json.load(file)
print(data)                   #印出字典資料
print('name:',data['name'])
print('ver:',data['how old'])

data['name']='new name'#修改字典資料
#最新資料複寫回檔案
with open('config.json',mode='w') as file:
    json.dump(data,file)














