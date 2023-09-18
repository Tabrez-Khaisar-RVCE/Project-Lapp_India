import mysql.connector
# from collection import deque

db = mysql.connector.connect(
    host="HOST_NAME",
    user="JUSER_NAME",
    passwd="Password",
    database="db_name"
)

# import mysql.connector
# from textblob import TextBlob
#
# db = mysql.connector.connect(
#     host="HOST_NOMBER",
#     user="USER",
#     password="Password",
#     database="db_name"
# )
mycursor = db.cursor()
# def User_Details():
#   mycursor.executemany("INSERT INTO User_Details (Username, Email_ID, Plant_ID, Access_Level, Password) VALUES(%s,%s,%s,%s,%s)",
#                      [("Affan", "affanahmed2000@gmail.com", "6186", 3, 'Gadget'), ("Shirish", "shirishkumar.lapp@gmail.com", "6186", 3, 'Password.123'), ("Tabrez", "Tabrez.lapp@gmail.com", "6186", 3, 'Tabrez@Lapp'), ("Muzakkir", "Muzakkirjlapp@gmail.com", "6186", 3, 'Password.123')])
#   db.commit()

# def hold_WO_SQL():
#
#   mycursor.execute("SELECT Work_Order_Number, LAPP_Part_Number FROM Work_Order_Details")
#   db.commit()
#   myresult = mycursor.fetchall()
#   db.commit()
#   myresult.reverse()
#   for x in myresult:
#   print(x[1])


# # hold_WO_SQL()
#
# a = input(Enter)
# list = [("a", "b", "c", "d", "e"), ("s", "g", "h", "k", "l")]

# integer 0,10,20,
# latest 10 VALUES
# next 10 values
# [Date, Time, Parameter, data changed, Operation]
# [Parameters, Previous_Value, Updated_Value]

# def commit_WO(list):
#     for x in list:
#         mycursor.execute(
#             "INSERT INTO Work_Order_Details (Work_Order_Number, LAPP_Part_Number, Material_Description, Order_Quantity_GMEIN, Delivered_Quantity_GMEIN) VALUES(%s,%s,%s,%s,%s)", x)
#         db.commit()

#
#
# def commit_IT(list):
#     for x in list:
#         mycursor.execute(
#             "INSERT INTO Inspection_Table (Lapp_Part_Number, Ballon_Number, Spec_Details, LSL, USL, Instruments_Used) VALUES(%s,%s,%s,%s,%s,%s)", x)
#         db.commit()
#
#
# def commit_PI(list):
#     for x in list:
#         mycursor.execute(
#             "INSERT INTO Purchase_Input (Lapp_Part_Number, Supplier_Part_Number, Supplier_Name, Purchase_Order, GRN_Number, Quantity_Batch) VALUES(%s,%s,%s,%s,%s,%s)", x)
#         db.commit()
# def commit_MB(list):
#     for x in list:
#         mycursor.execute(
#             "INSERT INTO Master_BOM (FG_Part_Number , Description, Customer , Special_Instruction_Cutting , Special_Instruction_Assembly , Special_Instruction_Crimping, Drawing_Rev , Date_and_Time , Special_Instruction_Cutting, Special_Instruction_Crimping , Special_Instruction_Assembly) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", x
#         )
#         db.commit()

# def Plant_Details(list):
#     for x in list:
#         mycursor.execute(
#             "INSERT INTO Plant_Details (Plant_ID, Operation_Type, Process_Type, Machine_Type, Machine_Tool_Number VALUES(%s,%s,%s,%s,%s)", x)
#         db.commit()

# def Assembly(list):
#     for x in list:
#         mycursur.execute(
#         "INSERT INTO Assembly (Component_Number ,Cable_Sl_Number ,Process ,Testing_Machine_Board_No) VALUES(%s,%s,%s,%s)", x)
#         )
#         db.commit()

# def Cable_Cutting(list):
#    for x in list:
#   mycursor.executemany("""INSERT INTO Cable_Cutting ( component_part_number, Cable_sl, Cable_desc, cut_length, qty, cut_tool, JACKET_TOOL, Jacket_FE, Jacket_TE, Strip_Tool, Strip_FE, Strip_TE,core_color)
#         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", x)
#   db.commit()

# def Crimping(list):
#   for x in list:
# mycursor.execute("INSERT INTO Crimping ( Component_Number ,Cable_Sl_Number,FE_Marker_Details,FE_Marker_PN,FE_Terminal_PN,FE_Crimp_Details,FE_Marker_Length,FE_Crimp_Height,FE_Pull_Force,FE_Marker_Instruction,TE_Marker_Details,TE_Marker_PN,TE_Terminal_PN,TE_Crimp_Details,TE_Marker_Length,TE_Crimp_Height,TE_Pull_Force,TE_Marker_Instruction) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
#                  ("Affan", "affanahmed2000@gmail.com", "6186", '3', 'Gadget', "Shirish", "shirishkumar.lapp@gmail.com", "6186", '3', 'Password.123', "Tabrez", "Tabrez.lapp@gmail.com", "6186", '3', 'Tabrez@Lapp', "6186", '3', 'Tabrez@Lapp'))
# db.commit()
#
# def Commit_UD(list):
# for x in list:
#     mycursor.executemany("INSERT INTO User_Details (Username, Email_ID, Plant_ID, Access_Level, Password) VALUES(%s,%s,%s,%s,%s)",x)
#
#     db.commit()


# def commit_junction(list):
#     for x in list:
#         mycursor.executemany(
#             "INSERT INTO Junction (FG_Part_Number, Component_Number, Cable_Sl_Number) VALUES(%s,%s,%s)", x)


#   mycursor.executemany(
#     """INSERT INTO Assembly (Component_Number, Cable_Sl_Number, Process, Testing_Machine_Board_No) VALUES(%s,%s,%s,%s)""", ('3', '3', 'Muzakkir', 'Muzakkirjlapp@gmail.com'))
#    db.commit()


# commit_WO(list)
# mycursor.execute("ALTER TABLE Changes ADD Index INT UNSIGNED NOT NULL AUTO_INCREMENT")
# db.commit()


def call_Crimp():
    mycursor.execute(
        "SELECT * FROM Crimping")

    d = mycursor.fetchall()
    print(d)
    return d


call_Crimp()
# def Fetch(value_WO):  # fetch data
#
#     mycursor.execute(
#         "SELECT * FROM Work_Order_Details WHERE Work_Order_Number=%s", (value_WO,))
#     d = mycursor.fetchall()
#
#     print(d)
#
#     a = d[0][4]
#     print(a)


# Fetch('SP1010')


# mycursor.execute(
#     "SELECT Work_Order_Number FROM Work_Order_Details")
# d = mycursor.fetchall()
# d1 = []
# for i in d:
#     d1.append(i[0])
# print(d1)
# mycursor.execute(
#     "UPDATE Work_Order_Details SET WO_Qty_Remaining=%s WHERE Work_Order_Number=%s", (a, value_WO))
# db.commit()
# Join command:
# mycursor.execute(
#     """SELECT work_order_details.Work_Order_Number work_order_details.FG_Part_Number, master_bom.Customer, master_bom.Description
#     FROM Work_Order_Details
#     INNER JOIN Master_BOM
#     ON Work_Order_Details.FG_Part_Number=Master_BOM.FG_Part_Number""")

# change password function:


# def update_password(email, new_pswd):
#
#     mycursor.execute("UPDATE User_Details SET Password=%s WHERE Username=%s", (new_pswd, email))
#     db.commit()
#
#
# update_password("SP1010", "565")
