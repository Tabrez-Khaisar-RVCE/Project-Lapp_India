import random
import math
from email.message import EmailMessage
import smtplib

import pandas as pd
from BACKEND_DB import fetch_WO
from BACKEND_DB import updatedb
from BACKEND_DB import updatingqty

def WO_Excel_Input_py(file_location):
    try:
        col_list=['Order','Material Number','Material description','Order quantity (GMEIN)','Delivered quantity (GMEIN)']
        wo_sap_sheet = pd.read_excel(file_location[0],usecols=col_list)
        w_order_db=fetch_WO()
        list_of_tuples =w_order_db
        list_of_lists = [list(elem) for elem in list_of_tuples]
        # print(list_of_lists)
        b=[int(x[0]) for x in w_order_db]
        match_sap=[]
        for index, row in wo_sap_sheet.iterrows():
            if row["Order"] in b:
                # print(list(row))
                match_sap.append(list(row))
        # print(match_sap)
        non_match = []
        # print("\n\t\t\t\t\t\t\t\t\t LIST OF NON MATCHING DATA \n")
        for index, row in wo_sap_sheet.iterrows():
            if row["Order"] not in b:
                # print(list(row))
                non_match.append(list(row))
        q=non_match
        updatedb(q)
        # print(non_match)
        qty=[]
        for i in match_sap:
            for j in list_of_lists:
                j[0]=int(j[0])
                if(i[0]==j[0]):
                    # print("hi")
                    if(i[4]>j[4]):
                        # print("yes")
                        updatingqty(i[4],j[0])
                    # else:
                        # print("NO")
        return [True]

    except ValueError:
        return [False,'Columns are wrong']

    except FileNotFoundError:
        return [False,'Not an excel file']


def email_alert(to):
    try:
        OTP=str(random.randint(100000,999999))

        subject='OTP - Lapp Ölflex Connect App'
        body='OTP: '+ OTP
        msg=EmailMessage()
        msg.set_content(body)
        msg['subject']=subject
        msg['to']=to

        user="EmailId"
        msg['from']=user
        password="PASSWORD"

        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(user,password)
        server.send_message(msg)

        server.quit()
        return [True,OTP]
    except:
        return [False,11001] #Improve multiple error handling
