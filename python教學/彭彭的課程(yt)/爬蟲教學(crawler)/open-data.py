#網路連線
# import urllib.request as re
# src='https://data.taipei/#/dataset/detail?id=0a1f284d-e985-4c39-b0b5-53389fbfa6e9'
# with re.urlopen(src) as res:
#     data=res.read().decode('utf-8')  #解碼網站中的中文字
# print(data)    #取得網站原始碼


#串接，擷取公開資料  #open abl  #json檔

import urllib.request as re
import json
src='https://data.ntpc.gov.tw/api/datasets/4A03827A-588B-4058-AB21-EC02283E2BB7/json?page=0&size=100'
with re.urlopen(src) as res:
    data=json.load(res)
# print(data) 
   #取得網站原始碼
with open('分館.txt',mode="w",encoding="utf-8") as file:
    for cc in data:
        file.write(cc['Reading_Room']+'\n') #擷取圖書館分館名稱