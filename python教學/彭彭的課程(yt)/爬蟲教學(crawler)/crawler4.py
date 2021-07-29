import urllib.request as re
def page(n):
    request=re.Request(n,headers={
    'cookie':'_ga=GA1.2.479863600.1556030004; _gid=GA1.2.766760695.1624536012; __cf_bm=7f8e45c20f67da2f372ba2f389d0ecd7e6f47b2b-1624693983-1800-AfPVyA9VbyGlF1IQCxc1u/tM0DCFC3uUhnkTjAarhLbjL7Q7qSbWjZYDlegOdVUWiK1I7KPxO3TjYB6cKqAfcls=',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'

    })
    with re.urlopen(request) as res:
        p=res.read().decode('utf-8')
    # print(p)

    import bs4
    root=bs4.BeautifulSoup(p,'html.parser')
    titles=root.find_all('div',class_="title")
    for title in titles:
        if title.a !=None:
            print(title.a.string)

    next=root.find('a',string='‹ 上頁')
    return next['href']
paeurl='https://www.ptt.cc/bbs/NBA/index6529.html'
count=0
while count<5:
    paeurl='https://www.ptt.cc'+page(paeurl)
    count+=1