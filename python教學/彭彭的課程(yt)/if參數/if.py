#s=[5,2,1,2,1,1]
#print(s[0])


#dis={s:s**2 for s in [3,4,5]}
#print(dis)


s=int(input('輸入數字?'))

if s>200:
    print('大等於200')
elif s>100:
    print('小於200，大於等於100')
else:
    print('小於100')