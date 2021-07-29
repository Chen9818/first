


import os                             #找尋檔案是否存在
# h=os.path.expanduser("~")
# p=os.path.join(h,"Picture","金融交易的天堂和地獄_200404_0004jj.jpg")
# print(p)

# s=r'C:\windows\picture\30715.jpg'   #確認路徑是否為檔案?
# y=os.path.isfile(s)
# print(y)


# u=r'C:\windows\picture'      #確認路徑是否為資料夾?
# y=os.path.isdir(u)
# print(y)


import shutil

total,used,free=shutil.disk_usage('.')
gb=2**30
print('磁碟容量:{:.2f}GB'.format(total/gb))
print('已使用:{:.2f}GB'.format(used/gb))
print('目前容量:{:.2f}GB'.format(free/gb))





import time           
t=time.time()    #1970/1/1至今的秒數
print(t)

n=time.localtime()      #將秒數換算現在日期
print(n)


import argparse
parser = argparse.ArgumentParser()
parser.add_argument("arg1")
parser.add_argument("arg2",
                    help="這是第 2 個引數，請輸入整數")
parser.add_argument("arg3",
                    help="這是第 3 個引數，「要求」輸入整數",
                    type=int)
args = parser.parse_args()
print('第一個數',args.arg1)
print('第二個數',args.arg2)
print('第三個數',args.arg3)

