i=0
while i<5:
    print('*')
    i+=1





rl=['how old?','how much','tast like?','shit is?']
al=['9','100','shit','poop']
score=0
total=len(rl)
h=0


while h<total:
    r=rl[h]
    a=al[h]
    h+=1

    print(r,end='    ')
    ans=input().lower().strip()

    if ans==a:
        score+=25
        print('good')
    else:
        print('bad')
    print()#題目空行
print('總分:',score)




#rl=['how old?','how much','tast like?','shit is?']
# al=['9','100','shit','poop']
# score=0
# for q,a in zip(rl,al):
#     print(q,end='      ')
#     c=input().lower().strip()

#     if c==a:
#         score+=25
#         print('goooooooooo')
#     else:
#         print('bad')


# print('total:',score)