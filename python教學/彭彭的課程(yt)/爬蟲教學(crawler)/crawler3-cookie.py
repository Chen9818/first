import urllib.request as re
def getdata(url):

    request=re.Request(url,headers={
        'cookie':'_ga=GA1.2.479863600.1556030004; _gid=GA1.2.766760695.1624536012; __cf_bm=ff44a5c493882dcb0f9ee698458bf84c8531d4ab-1624609223-1800-AQjkU2iFJqDTObj90tngTVj8SqIzVGUGqqmpIJ4KDIXvgILsw7vvQ+ySfL70CjTvbXGWoTG/o0MmvIXMGLLKATM=; over18=1',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'})
    with re.urlopen(request) as q:
        o=q.read().decode('utf-8')
    # print(o)

    import bs4
    oo=bs4.BeautifulSoup(o,'html.parser')
    titles=oo.find_all('div', class_="title")
    for title in titles:
        if title.a !=None:
            print(title.a.string)

    #抓取上一頁連結
    nextlink=oo.find('a',string='‹ 上頁')  #找到內文是‹ 上頁的a標籤
    return nextlink['href']   #把資料從函式取出

pageurl='https://www.ptt.cc/bbs/Gossiping/index.html'
count=0
while count<5:     #抓五頁
    pageurl='https://www.ptt.cc'+getdata(pageurl)    #下一頁完整的網址
    count+=1


