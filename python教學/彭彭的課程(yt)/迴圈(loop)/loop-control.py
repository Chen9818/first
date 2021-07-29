# break範例
n=0
while n<5:
    if n==3:
        break
    print(n)  #印出迴圈中的n
    n+=1
print('最後的',n)  #印出最後的n

#ctrl+shift旁的斜線可以快速註解

#continue範例
# n=0
# for x in [0,1,2,3]:
#     if x%2==0:
#         continue
#     print(x)
#     n+=1
# print("最後的",n)

#else範例
# sum=0
# for n in range(11):
#     sum=sum+n
# else:
#     print(sum)  #印出0+1+2+........+10

#找出整數平方根
n=input('輸入一個整數:')
n=int(n)
for i in range(n):
     if i*i==n:
         print('整數平方根:',i)
         break
else:                          #用break強制結束迴圈時，不會執行else區塊
     print("沒有整數平方根")

