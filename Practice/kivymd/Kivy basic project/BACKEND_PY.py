# import random
# import math
# from email.message import EmailMessage
# import smtplib
#
# def email_alert(to):
#     try:
#         OTP=str(random.randint(100000,999999))
#
#         subject='OTP - Lapp Ölflex Connect App'
#         body='OTP: '+ OTP
#         msg=EmailMessage()
#         msg.set_content(body)
#         msg['subject']=subject
#         msg['to']=to
#
#         user="muzakkirjlapp@gmail.com"
#         msg['from']=user
#         password="dajqgvhpjjvmmzxl"
#
#         server = smtplib.SMTP("smtp.gmail.com",587)
#         server.starttls()
#         server.login(user,password)
#         server.send_message(msg)
#
#         server.quit()
#         return [True,OTP]
#     except:
#         return [False,11001] #Improve multiple error handling
