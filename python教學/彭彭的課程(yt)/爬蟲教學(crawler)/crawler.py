#抓取ptt網頁原始碼(html)
import urllib.request as re
src='https://forum.gamer.com.tw/B.php?bsn=4373'
#建立一個request物件，附加Request headers的資訊
request=re.Request(src, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'})

with re.urlopen(request) as res:
    data=res.read().decode('utf-8')
# print(data)

 #解析原始碼，取得文章標題
import bs4
root=bs4.BeautifulSoup(data,'html.parser')
titles=root.find_all('div',class_="b-list__tile")
for title in titles:
     if title.p !=None:
         print(title.p.string)
        # da=title.a.string 
        # with open('nba.txt',mode='w',encoding='utf-8') as dd:
        #         dd.write(da)

