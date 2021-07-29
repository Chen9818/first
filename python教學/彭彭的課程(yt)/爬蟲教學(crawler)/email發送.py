#寄送email程式
import email.message
msg=email.message.EmailMessage()
msg['from']='wwenba2k@gmail.com'  #寄件人
msg['to']='wwenba3k@gmail.com'    #收件人
msg['subject']='hi'  #標題
#寄送純文字內容
# msg.set_content('測試')
#寄送多樣化內容(html)
msg.add_alternative('<h1>大優惠</h1>快來',subtype='html')

#連線到SMTP server 驗證寄件人身分並發送郵件
import smtplib
#到網路上搜尋gmail smtp server
server=smtplib.SMTP_SSL('smtp.gmail.com',465)
server.login('wwenba2k@gmail.com','sobavtcxozihachh')   
#帳號，密碼 ===> 去google帳號內產生一個應用程式密碼
server.send_message(msg)
server.close()

