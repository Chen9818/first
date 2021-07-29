import random
kk=['33','88']
print(random.choice(kk))      #隨機從列表選出一元素
print(random.randint(1,10))   #從1-10
print(random.randrange(11))   #從0-10
random.shuffle(kk)          
print(kk)                     #印出列表的隨機組合

random.seed()                 #seed是只初始化隨機種子，簡單來說抽之前先攪拌一下
for l in range(10):
    print(random.randrange(11))











for o in range(11):
    print(o)
