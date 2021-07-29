#抓取kkday網頁原始碼(ajax)
import urllib.request as re
src='https://m.kkday.com/zh-tw/area_api/ajax_get_product_tags'
#建立一個request物件，附加Request headers的資訊
request=re.Request(src, headers={
    'cookie':'KKUD=4b8260068d649293fc3e7716e27fa7d0; _gcl_au=1.1.131448257.1624698439; _gid=GA1.2.1266780493.1624698441; _hjTLDTest=1; _hjFirstSeen=1; _hjid=b722c2f5-6628-4711-9767-c43c3ddc500c; _hjAbsoluteSessionInProgress=0; csrf_cookie_name=8e6cbd594ec4dad77f322296336926aa; country_lang=zh-tw; lang_ui=zh-tw; currency=TWD; ci_session=a%3A4%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%22f129a99decf7e343d72567b682ab7ba6%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A13%3A%221.164.244.144%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A120%3A%22Mozilla%2F5.0+%28Linux%3B+Android+6.0%3B+Nexus+5+Build%2FMRA58N%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F91.0.4472.114+Mobil%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1624699124%3B%7Db96f0eb5cd4061104f2b905077070e8a; _dc_gtm_UA-49763723-1=1; _dc_gtm_UA-117438867-1=1; mp_b8150a8ddf736c19fdc0f146b9ffac24_mixpanel=%7B%22distinct_id%22%3A%20%2217a4793037b170-09eadd72bcfa19-6373267-144000-17a4793037c461%22%2C%22%24device_id%22%3A%20%2217a4793037b170-09eadd72bcfa19-6373267-144000-17a4793037c461%22%2C%22Platform%22%3A%20%22www.kkday.com%22%2C%22LoginChannel%22%3A%20%22NO%22%2C%22DisplayCurrency%22%3A%20%22TWD%22%2C%22DisplayLang%22%3A%20%22zh-tw%22%2C%22DisplayCountry%22%3A%20%22TW%22%2C%22IsInternal%22%3A%20false%2C%22Cid%22%3A%20null%2C%22Ud1%22%3A%20null%2C%22Ud2%22%3A%20null%2C%22MemberUuid%22%3A%20%22%22%2C%22Kkud%22%3A%20%224b8260068d649293fc3e7716e27fa7d0%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.kkday.com%2Fzh-tw%2Fkk%2Fajax_get_announcement_config%25E4%25BD%2586%25E5%25A5%25B9%25E5%2587%25BA%25E7%258F%25BE%25E9%258C%25AF%25E8%25AA%25A4%22%2C%22%24initial_referring_domain%22%3A%20%22www.kkday.com%22%2C%22%24search_engine%22%3A%20%22google%22%7D; _ga=GA1.1.1975757923.1624698441; _uetsid=f2ed6f50d65d11ebb99009b088990b78; _uetvid=f2edb3f0d65d11ebbf88613d39e62abb; _ga_RJJY5WQFKP=GS1.1.1624698454.1.1.1624699182.3; AWSALBTG=S/99fQLxIU43UL/ABh/gxtfFLWsd7QZocs2szcuI0qYQ8gMPJP0vkgDCWxR/D13DEa4Ts5mzLi0G/bzVcTW2D+3Pp6RMplUUHezK/jB4+wUCujp6uYrVRYu2d9j0O62nXnc3uOlkfaJDrOBlSY8iMO1Tytd9o8mHuXp9HMGMcCb4; AWSALBTGCORS=S/99fQLxIU43UL/ABh/gxtfFLWsd7QZocs2szcuI0qYQ8gMPJP0vkgDCWxR/D13DEa4Ts5mzLi0G/bzVcTW2D+3Pp6RMplUUHezK/jB4+wUCujp6uYrVRYu2d9j0O62nXnc3uOlkfaJDrOBlSY8iMO1Tytd9o8mHuXp9HMGMcCb4',
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36'})

with re.urlopen(request) as res:
    data=res.read().decode('utf-8')
# print(data)

 #解析原始碼，取得文章標題
#解析json
import json
datas=json.loads(data)
# print(datas)

posts=datas['data']
for key in posts:
    print(key['name'])