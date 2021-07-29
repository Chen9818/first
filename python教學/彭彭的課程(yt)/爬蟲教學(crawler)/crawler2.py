import urllib.request as re
url='https://www.netflix.com/browse/my-list'
req=re.Request(url,headers={'cookie':'memclid=8dea062b-9cde-4ba7-b696-e16f1eaedefb; pas=%7B%22supplementals%22%3A%7B%22muted%22%3Afalse%7D%7D; nfvdid=BQFmAAEBEPIBlqbPTtt4q5X3HUgasrNgAVKzNbG5wQb8SSdQ6YK1w6GPUxr_HcvXrHJogMz-vmVdF55Nf55gFJotkfDt3lPWH-WkUL7shy0_HtU61FJDL2lT4ceG9aYwIGIMOXx0hJKZgFVDQoXIuVh6IcaWs6aa; OptanonConsent=isIABGlobal=false&datestamp=Thu+May+06+2021+21%3A11%3A52+GMT%2B0800+(%E5%8F%B0%E5%8C%97%E6%A8%99%E6%BA%96%E6%99%82%E9%96%93)&version=6.6.0&consentId=d19b0b36-bb8d-4e36-8bbe-7bb359fd923a&interactionCount=0&landingPath=https%3A%2F%2Fhelp.netflix.com%2Fzh-tw%2F&groups=C0001%3A1%2CC0002%3A1%2CC0004%3A1&hosts=H1%3A1%2CH2%3A1%2CH12%3A1%2CH13%3A1%2CH27%3A1%2CH28%3A1%2CH30%3A1; SecureNetflixId=v%3D2%26mac%3DAQEAEQABABRTpzwYKf0hn-NIaJRGrVDGbE8ezqkm7MQ.%26dt%3D1624546014430; NetflixId=v%3D2%26ct%3DBQAOAAEBEOmW3KuI_ewMY8Wg12vuOiuB4CpE2Y2pIjUSZ3_FOF0T84Dy2ZMmS48jXrVnBAAnZjtyHmr74GxEIXSXXMkvzgsP7vmjdSRAREjDyz7EaR7-Up6K5wr5uD9BY9hkkX4X5jDRjsnN3DURzD7GyEieM8wXXqr2r-yPY_VP0mkZhiLErkt6Qx63PJPGchGi-9lYuqq389zA9du99tOimfRUOd7LkYEjH0tZHuntq-Tz6URLAFO303zRH-78psGItnx5MoOL5Yvogd05ufD5f0WmLBxbW4tvjj6_un5qWn6wT5OGyPNqjFmt7HhNi-kii7X79tdIAklDYMy9o_Tisw0Nrmuk007hRrucLWDtjrzxBuo-tHCeW8nxpkR_WBSnEu98jVxpJHMFJhacp3TCvbNHTOt6h3yUVFBMzkS7rYTAeBVRmseiYWFLwwNGahCm8K6XlrWdANbT5bI5w3tJw00PffuIONsusAKGMQWD96fRJ2HHv951SHVTK3YFXOez-gMSnZXQCCkJ4iM_AkYlWc3NQgE6eVDpFFYAcPc-WScs7wsDp4RHRzTvNJu9k9Yr3pQDN19Dq4tfvF0-_ZJKdnwEVNmWVDMxswWYDyN-gKR_cSjJw0mgzBWh24ZRP1ZSKIyj5qhFbjlOcQE2Ma22tzJDKxXZsA..%26bt%3Ddbl%26ch%3DAQEAEAABABSjsAgCv6jfKE_d8K59m7s0sz71GlJC9m8.%26mac%3DAQEAEAABABRCjwpWoxKkW0b_tEz6GfiHWGWQxpFtNp4.; profilesNewSession=0; clSharedContext=5dc318fe-95cf-493f-98c2-1685930f95d9; playerPerfMetrics=%7B%22uiValue%22%3A%7B%22throughput%22%3A7997.09%2C%22throughputNiqr%22%3A0.6605884533489501%7D%2C%22mostRecentValue%22%3A%7B%22throughput%22%3A7997.09%2C%22throughputNiqr%22%3A0.6605884533489501%7D%7D','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'})
with re.urlopen(req) as s:
     se=s.read().decode('utf-8')
# print(se)

import bs4
root=bs4.BeautifulSoup(se,'html.parser')
titles=root.find_all('div',class_="ptrack-content")
for title in titles:
     if title.a !=None:
         print(title.a['aria-label'])
    
# print(titles)