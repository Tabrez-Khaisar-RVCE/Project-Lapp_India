import mysql.connector
from textblob import TextBlob

# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="password.123.123",
#     database="tr_db"
# )
# mycursor = db.cursor()

db = mysql.connector.connect(
    host="HOST_NUMBER",
    user="USER_NAME",
    password="PASSWORD",
    database="DATABASE"
)
mycursor = db.cursor()


def validate_user_db(username, password):

    return [True, True, 'Shirsh', '6186', '3']  # Temprorary hold
    mycursor.execute("SELECT * FROM User_Details WHERE Email_ID=%s", (username,))
    details = mycursor.fetchall()
    if len(details) != 0 and password == details[0][4]:

        return [True, True, details[0][0], details[0][2], details[0][3]]

    elif len(details) != 0 and password != details[0][4]:

        return [True, False]

    elif len(details) == 0:
        return [False, False]


def update_password(email, new_pswd):
    mycursor.execute("UPDATE User_Details SET Password=%s WHERE Email_ID=%s", (new_pswd, email))
    db.commit()


def WO_details_db(WO):
    mycursor.execute(
        "SELECT  FG_Part_Number,WO_QTY_Delivered,WO_Qty_Total FROM Work_Order_Details WHERE Work_Order_Number=%s", (WO,))
    d = mycursor.fetchall()
    if d == []:return [False]
    else:
        d = list(d[0])
        return d


def fetch_WO():
    mycursor.execute(
        "SELECT * FROM Work_Order_Details")
    d = mycursor.fetchall()
    d1 = []
    for i in d:
        d1.append(i)
    return d1


def updatingqty(qty, x):
    mycursor.execute(
        "UPDATE work_order_details SET WO_QTY_Delivered =%s WHERE Work_Order_Number =%s", (qty, x))
    db.commit()


def updatedb(nonmatchlist):
    for x in nonmatchlist:
        mycursor.execute(
            "INSERT INTO Work_Order_Details (Work_Order_Number, FG_Part_Number, Material_Description, WO_Qty_Total, WO_QTY_Delivered) VALUES(%s,%s,%s,%s,%s)", x)
    db.commit()

def Modify_WO_recheck_db(WorkOrder,Qty):
    mycursor.execute(
        "SELECT Work_Order_Number, FG_Part_Number, Material_Description, WO_Qty_Total FROM Work_Order_Completed WHERE Work_Order_Number=%s", (WorkOrder,))
    d = mycursor.fetchall()
    d = list(d[0]) + [Qty]

    mycursor.execute("DELETE FROM Work_Order_Completed WHERE Work_Order_Number=%s", (WorkOrder,))

    mycursor.execute(
        "INSERT INTO Work_Order_Details (Work_Order_Number, FG_Part_Number, Material_Description, WO_Qty_Total, WO_QTY_Delivered) VALUES(%s,%s,%s,%s,%s)", d)
    db.commit()

def WO_details_completed_db(WO):
    mycursor.execute(
        "SELECT WO_Qty_Total FROM Work_Order_Completed WHERE Work_Order_Number=%s", (WO,))
    d = mycursor.fetchall()
    if d == []:return False
    else:
        d = list(d[0])
        return d


def Enter_UD_db(x):
    mycursor.execute(
        "INSERT INTO User_Details(Username, Email_ID, Plant_ID, Access_Level, Password) VALUES(%s,%s,%s,%s,%s)", x)
    db.commit()


def Retrieve_UD_db():
    mycursor.execute(
        "SELECT * FROM User_Details")
    return mycursor.fetchall()


def Drop_UD_db(email_id):
    mycursor.execute(
        "DELETE FROM User_Details WHERE Email_ID=%s", (email_id,))
    db.commit()


def Update_Email_ID_UD_db(list_of_details):
    mycursor.execute(
        "UPDATE User_Details SET Username=%s,Plant_ID=%s,Access_Level=%s WHERE Email_ID=%s", list_of_details)
    db.commit()

def Validate_Machine_Tool_id_db(Machine_tool_id):
    mycursor.execute(
        "SELECT Operation_Type FROM Plant_Details WHERE Machine_tool_id=%s", (Machine_tool_id,))
    op_t = mycursor.fetchall()
    if not op_t == []:
        return True
    else:
        return False


def Component_Details_db(Component_Number):
    mycursor.execute(
        "SELECT Component_Number FROM Component_Details WHERE EXISTS (SELECT Component_Number FROM Component_Details WHERE Component_Number=%s)", (
            Component_Number,))
    value_me = mycursor.fetchall()
    if not value_me == []:
        mycursor.execute(
            "SELECT Cable_desc,Core_Wire_Color FROM Component_Details WHERE Component_Number=%s", (Component_Number,))
        color_db = mycursor.fetchall()
        db_color = []
        for i, e in enumerate(color_db):  # making a list of colors
            db_color.append(e[1])
        return_desc = [True, color_db[0][0], db_color]
        return return_desc
    else:
        return [False]


def check_availability_FG_db(Part_Number):
    mycursor.execute(
        "SELECT Description FROM fg_details WHERE FG_Part_Number=%s", (Part_Number,))
    op_t = mycursor.fetchall()
    if not op_t == []:
        return True
    else:
        return False


def Validate_Terminal_PNO_db(Part_Number):
    mycursor.execute(
        "SELECT Strip_length FROM terminal_details WHERE Terminal_PN=%s", (Part_Number,))
    op_t = mycursor.fetchall()
    if not op_t == []:
        return True
    else:
        return False


def Modify_FG_Details(list_of_details):
    mycursor.execute(
        "UPDATE FG_Details SET Description=%s,Customer_name=%s,Special_Instruction_Cutting=%s,Special_Instruction_Crimping=%s,Special_Instruction_Assembly=%s,Drawing_Rev=%s WHERE FG_Part_Number=%s", list_of_details)
    db.commit()


def Enter_FG_Details(list):
    mycursor.execute(
        "INSERT INTO FG_Details(FG_Part_Number,Description,Customer_name,Special_Instruction_Cutting,Special_Instruction_Crimping,Special_Instruction_Assembly,Drawing_Rev) VALUES(%s,%s,%s,%s,%s,%s,%s)", list)
    db.commit()

def Enter_CD_db(x):
    mycursor.execute(
        "INSERT INTO Component_Details(Component_Number,Core_Wire_Color,Cable_desc) VALUES(%s,%s,%s)", x)
    db.commit()

def Delete_Component_details(Component_No, Core_Wire_Color):
    if Core_Wire_Color == "":
        mycursor.execute("DELETE FROM Component_Details WHERE Component_Number=%s", (Component_No,))
    else:
        mycursor.execute(
            "DELETE FROM Component_Details WHERE Component_Number=%s AND Core_Wire_Color=%s", (Component_No, Core_Wire_Color))
    db.commit()

def Retrieve_terminal_db(terminal_pn):
    mycursor.execute(
        "SELECT Strip_Length FROM Terminal_Details WHERE Terminal_PN=%s", (terminal_pn,))
    st = mycursor.fetchall()
    if st==[]:return None
    size_avg = int(len(st[0][0])/2)
# first Strip_length
    one_st = st[0][0][:size_avg]
# Second Strip_length
    two_st = st[0][0][size_avg+1:]
    Average = (float(two_st)-float(one_st))/2
    # Strip length
    strip_l = float(two_st)-Average
    tol_s = int(strip_l)-float(one_st)
    tol_b = float(two_st)-int(strip_l)
    return [strip_l, tol_s, tol_b]

def Modify_terminal_db(Details):
    Strip_Length_1 = float(Details[1])+float(Details[3])
    Strip_Length_2 = float(Details[1])-float(Details[2])
    Strip_length = str(Strip_Length_2)+"-"+str(Strip_Length_1)
    mycursor.execute("UPDATE Terminal_Details SET Strip_Length=%s WHERE Terminal_PN=%s",
                     (Strip_length, Details[0]))
    db.commit()

def Delete_terminal_db(terminal_pn):
    mycursor.execute("DELETE FROM Terminal_Details WHERE Terminal_PN=%s", (terminal_pn,))
    db.commit()

def Add_Terminal_db(Details):
    Strip_Length_1 = float(Details[1])+float(Details[3])
    Strip_Length_2 = float(Details[1])-float(Details[2])
    Strip_length = str(Strip_Length_2)+"-"+str(Strip_Length_1)
    mycursor.execute("INSERT INTO Terminal_Details(Terminal_PN, Strip_Length) VALUES(%s,%s)", (Details[0], Strip_length))
    db.commit()
