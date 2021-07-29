import re
text='連絡電話:0975655757，夜間關機。'
a=re.search('電話',text)
print(a)

match=re.search(r'09\d{8}',text)
if match:
    print('find:',match.group())
    print('起始索引編號:',match.start())
    print('結束索引編號:',match.end())
    
else:
    print('nope')