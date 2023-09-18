import mysql.connector
# from textblob import TextBlob

db = mysql.connector.connect(
    host="HOST_NUMBER",
    user="users",
    password="Password",
    database="db_name"
)
# mycursor.execute("Create DATABASE tr_db")
mycursor = db.cursor()


WO = "SP1021"


def WO_details_db(WO):
    mycursor.execute(
        "SELECT  FG_Part_Number,WO_Qty_Remaining,WO_Qty_Total FROM Work_Order_Details WHERE Work_Order_Number=%s", (WO,))
    d = mycursor.fetchall()
    print(d)
    if d == []:
        d.append(False)
        print(d)
    else:
        d = list(d[0])
        print(d)


# WO_details_db(WO)

def WO_db():
    mycursor.execute("SELECT * FROM Work_Order_Details")
    t_content = mycursor.fetchall()
    return t_content


WO_db()


def Enter_Plant_Details(list):
    for x in list:
        mycursor.execute(
            "INSERT INTO Plant_Details(Plant_ID_6186,Plant_ID_4647,Operation_Type,Machine_Type,Machine_tool_id) VALUES (%s,%s,%s,%s,%s)", x
        )
        db.commit()


def Enter_WO(list):
    for x in list:
        mycursor.execute(
            "INSERT INTO Work_Order_Details(Work_Order_Number, FG_Part_Number, Material_Description, WO_Qty_Total, WO_Qty_Remaining) VALUES (%s,%s %s,%s,%s ,%s )", x)
        db.commmit()


def Enter_UD(x):
    mycursor.execute(
        "INSERT INTO User_Details(Username, Email_ID, Plant_ID, Access_Level, Password) VALUES(%s,%s,%s,%s,%s)", x)
    db.commit()


def Fetch(value_WO):  # fetch data

    mycursor.execute(
        "SELECT * FROM Work_Order_Details WHERE Work_Order_Number=%s", (value_WO,))
    d = mycursor.fetchall()

    print(d)

    a = d[0][4]
    return a

# Update Wo


def Update_WO():
    Fetch(value_WO)
    mycursor.execute(
        "SELECT Work_Order_Number FROM Work_Order_Details")
    d = mycursor.fetchall()
    d1 = []
    for i in d:
        d1.append(i[0])
    print(d1)
    mycursor.execute(
        "UPDATE Work_Order_Details SET WO_Qty_Remaining=%s WHERE Work_Order_Number=%s", (a, value_WO))
    db.commit()


def Enter_TD(list):
    for x in list:
        mycursor.execute("INSERT INTO Terminal_Details(Terminal_PN, Strip_Length) VALUES(%s,%s)", x)
        db.commit()


def Enter_IT(list):
    for x in list:
        mycursor.execute(
            "INSERT INTO Inspection_Table(FG_Part_Number,Ballon_Number,Specification_Details,LSL,USL,Instruments_Used)", x)
        db.commit()


def Enter_Changes(list):
    for x in list:
        mycursor.execute(
            "INSERT INTO Changes(Username,Date,Time,Access_Level,Parameters,Previous_Value,Updated_Value) VALUES(%s,%s,%s,%s,%s,%s,%s)", x)
        db.commit()


def Enter_CD(list):
    for x in list:
        mycursor.execute(
            "INSERT INTO Component_Details(Component_Number,Cable_sl,Wire_Size,Core_Colour,Cable_desc) VALUES(%s,%s,%s,%s,%s)", x)
        db.commit()


def Enter_FG_Details(list):
    for x in list:
        mycursor.execute(
            "INSERT INTO FG_Details(FG_Part_Number,Description,Customer_name,Special_Instruction_Cutting,Special_Instruction_Crimping,Special_Instruction_Assembly,Drawing_Rev,Date_and_Time) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)", x)
        db.commit()


def Enter_FG_Assembly(list):
    for a in list:
        mycursor.execute("INSERT INTO FG_Assembly(Process) VALUES(%s)", a)
        db.commit()
        list_1 = list[1]
        for x in list_1:
            mycursor.execute(
                "INSERT INTO FG_Assembly(Component_Number,Cable_Sl_Number,Testing_Machine_Board_No) VALUES(%s,%s,%s)", x
            )
            db.commit()


def Enter_FG_Crimp_Details(list):
    mycursor.execute("SELECT FG_Part_Number FROM FG_Details")
    fg_p = mycursor.fetchall()
    for x in list:
        mycursor.execute(
            "INSERT INTO FG_Crimp_Details(FE_Marker_Part_no,FE_Marker_Details,FE_Crimping_Specification,FE_Terminal_PN,FE_Crimp_Height,FE_Pull_Force,FE_Crimp_Details,TE_Marker_Part_no,TE_Marker_Details,TE_Crimping_Specification,TE_Terminal_PN,TE_Crimp_Height,TE_Pull_Force,TE_Crimp_Details,Component_Number,Cable_sl,Core_Wire_Color) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", x
        )
        db.commit()


def Enter_FG_Cut_Details_N(list):
    for x in list:
        mycursor.execute("SELECT FG_Part_Number FROM FG_Details")
        fg_p = mycursor.fetchall()
        mycursor.execute(
            "INSERT INTO FG_Cut_Details(FG_Part_Number,Component_Number,Cable_sl,Description,Cut_length,Machine_tool_id,Jacket_FE,Jacket_TE) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)", x)
        db.commit()
        mycursor.execute(
            "INSERT INTO FG_Cut_Details(FG_Part_Number)", fg_p)
        db.commmit()


def Enter_FG_Cut_Details(list_C):
    for x in list_C:
        list_2 = list_C[7]
        mycursor.execute("SELECT FG_Part_Number FROM FG_Details")
        fg_p = mycursor.fetchall()
        mycursor.execute(
            "INSERT INTO FG_Cut_Details(FG_Part_Number,Component_Number,Cable_sl,Description,Cut_Machine_tool_id,Cut_length,Jacket_Machine_tool_id,Jacket_FE,Jacket_TE) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)", x)
        db.commit()
        for a in list_2:
            mycursor.execute(
                "INSERT INTO FG_Component_Data(Core_Wire_Color,FE_Strip,TE_Strip,Tool_FE,Tool_TE) VALUES(%s,%s,%s,%s,%s)", a)
            db.commit()
            mycursor.execute(
                "INSERT INTO FG_Component_Data(FG_Part_Number,Component_Number,Cable_Sl) VALUES(%s,%s,%s)", (fg_p, list_C[0], list_C[1]))
            db.commit()


def Enter_FG_Junction(list):
    for x in list:
        mycursor.execute(
            "INSERT INTO FG_Junction(FG_Part_Number,Component_Number,Cable_sl) VALUES(%s,%s,%s)", x)
        db.commit()


def update_password(email, new_pswd):
    if "@lapp.com" in email or "@lapp.india.com" in email:
        mycursor.execute("UPDATE User_Details SET Password=%s WHERE Username=%s", (new_pswd, email))
        db.commit()


def report(WO, FG, WO_Qty, JT_Qty, Plant_id):
    mycursor.execute("SELECT * FROM FG_Details WHERE FG_Part_Numbers=%s", (FG,))
    FG_d = mycursor.fetchall()
    print(FG_d)
    mycursor.execute("SELECT * FROM FG_Cut_Details WHERE FG_Part_Numbers=%s", (FG,))
    cut_d = mycursor.fetchall()
    print(cut_d)
    mycursor.execute("SELECT * FROM FG_Crimp_Details WHERE FG_Part_Number=%s", (FG,))
    crimp_d = mycursor.fetchall()
    print(crimp_d)


def Insert_FG(FG, CN):
    mycursor.execute("SELECT * FROM FG_Details WHERE FG_Part_Numbers=%s", (FG))
    FG_d = mycursor.fetchall()
    print(FG_d)

# [WO, FG, WO_Qty,JT_Qty,Plant_ID]


def Retrieve_FG_Details_db(list_fg):

    mycursor.execute("SELECT * FROM FG_Details WHERE FG_Part_Number=%s", (list_fg[1],))
    fg_d = mycursor.fetchall()
    if fg_d == []:
        return [False, "FG Part Number does not exist"]

    PI = "Plant_ID_" + list_fg[4]
# Cut details :
    mycursor.execute(
        "SELECT Component_Number,Cable_sl,Description,Cut_length,Jacket_FE,Jacket_TE FROM FG_Cut_Details WHERE FG_Part_Number=%s", (list_fg[1],))
    fg_c_draft = mycursor.fetchall()
    fg_c = []
# cut list:
    for i, e in enumerate(fg_c_draft):
        fg_c_i = list(fg_c_draft[i])
        fg_c.append(fg_c_i)
#
    mycursor.execute(
        "SELECT Cut_Machine_id FROM FG_Cut_Details WHERE FG_Part_Number=%s", (list_fg[1]))
    fg_c_id = mycursor.fetchall()
    c_t_n = []
    for i, e in enumerate(fg_c_id):
        mycursor.execute("SELECT %s FROM Plant_Details WHERE Machine_tool_id=%s", (PI, fg_c_id[i]))
        c_t_ni = mycursor.fetchall()
        c_t_n.append(c_t_ni)

    mycursor.execute(
        "SELECT Jackeet_Machine_id FROM FG_Cut_Details WHERE FG_Part_Number=%s", (list_fg[1]))
    fg_j_id = mycursor.fetchall()
    j_t_n = []
    for i in fg_j_id:
        mycursor.execute("SELECT %s FROM Plant_Details WHERE Machine_tool_id=%s", (PI, fg_j_id[i]))
        j_t_ni = mycursor.fetchall()
        j_t_n.append(j_t_ni)
    for i, e in enumerate(fg_c):
        e.insert(4, c_t_n[i])
        e.insert(5, j_t_n[i])
        fg_c[i] = e
# Getting component details:
    for i, e in enumerate(fg_c):
        mycursor.execute(
            "SELECT Core_Wire_Color,FE_Strip,TE_Strip,Tool_FE,Tool_TE FROM FG_Component_Data WHERE FG_Part_Number=%s AND Component_Number=%s AND Cable_Sl=%s", (
                list_fg[1], e[0], e[1]))
        fg_r = mycursor.fetchall()
        e.append(fg_r)

# Crimp list:

    mycursor.execute(
        "SELECT FE_Marker_Part_no,FE_Marker_Details,FE_Crimping_Specification,FE_Terminal_PN,FE_Crimp_Height,FE_Pull_Force,FE_Crimp_Details,TE_Marker_Part_no,TE_Marker_Details,TE_Crimping_Specification,TE_Terminal_PN,TE_Crimp_Height,TE_Pull_Force,TE_Crimp_Details,Component_Number,Cable_sl,Core_Wire_Color FROM FG_Crimp_Details WHERE FG_Part_Number=%s", (list_fg[1],))
    fg_crp = mycursor.fetchall()
    fg_cr = []
    for i, e in enumerate(fg_cr):
        fg_cr.append(e)
# Assembly list
    for i, e in enumerate(fg_c):
        mycursor.execute(
            "SELECT * FROM FG_Assembly WHERE FG_Part_Number=%s AND Component_Number=%s AND Cable_Sl=%s", (list_fg[1], e[0], e[1]))
        fg_a_1 = mycursor.fetchall()
    # collecting process column elements
    fg_a_p = []
    for i, e in enumerate(fg_a_1):
        fg_a_p.append(e[4])
# collecting details
    fg_a_c = []
    for i, e in enumerate(fg_a_1):
        a = list(e)  # converting tuple to list
        a.pop(4)
        fg_a_c.append(a)
    fg_a = []
    for i, e in enumerate(fg_a_p):
        fg_a_t = [e, fg_a_c[0]]
        fg_a.append(fg_a_t)
    report_output(fg_d, fg_c, fg_cr, fg_a)
    return True


# def fg_backend_py(fg_d, fg_c, fg_cr, fg_a_p, fg_a_c):


# list_fg = [WO, FG, WO_Qty, JT_Qty, Plant_ID]
# mycursor.execute("SELECT * FROM FG_Details WHERE FG_Part_Number=%s", (list_fg[1]))
# fg_d = mycursor.fetchall()
# PI = "Plant_ID_"+list_fg[4]
# # Cut details :
# mycursor.execute(
#     "SELECT Component_Number,Cable_sl,Description,Cut_length,Jacket_FE,Jacket_TE FROM FG_Cut_Details WHERE FG_Part_Number=%s", (list_fg[1]))
# fg_c_draft = mycursor.fetchall()
# fg_c = []
# # cut list:
# for i, e in fg_c_draft:
#     fg_c_i = list(fg_c_draft[i])
#     fg_c.append(fg_c_i)
# #
# mycursor.execute(
#     "SELECT Cut_Machine_id FROM FG_Cut_Details WHERE FG_Part_Number=%s", (list_fg[1]))
# fg_c_id = mycursor.fetchall()
# c_t_n = []
# for i, e in enumerate(fg_c_id):
#     mycursor.execute("SELECT %s FROM Plant_Details WHERE Machine_tool_id=%s", (PI, fg_c_id[i]))
#     c_t_ni = mycursor.fetchall()
#     c_t_n.append(c_t_ni)
#
# mycursor.execute(
#     "SELECT Jackeet_Machine_id FROM FG_Cut_Details WHERE FG_Part_Number=%s", (list_fg[1]))
# fg_j_id = mycursor.fetchall()
# j_t_n = []
# for i in fg_j_id:
#     mycursor.execute("SELECT %s FROM Plant_Details WHERE Machine_tool_id=%s", (PI, fg_j_id[i]))
#     j_t_ni = mycursor.fetchall()
#     j_t_n.append(j_t_ni)
# for i, e in enumerate(fg_c):
#     e.insert(4, c_t_n[i])
#     e.insert(5, j_t_n[i])
#     fg_c[i] = e
#
# fg_e = []
# for i, e in enumerate(fg_c):
#     mycursor.execute(
#         "SELECT Core_Wire_Color,FE_Strip,TE_Strip,Tool_FE,Tool_TE FROM FG_Component_Data WHERE FG_Part_Number=%s AND Component_Number=%s AND Cable_Sl=%s", (
#             list_fg[1], e[0], e[1]))
#     fg_r = mycursor.fetchall()
#     e.append(fg_r)
#     fg_e.append()
# print(fg_e)

def Insert_C_Cr_A(list_l):

# Insert FG_Cut_Details:
    for i, e in list_l[3]:
        cut_legth_1 = float(e[2])+float(e[4])
        cut_legth_2 = float(e[2])-float(e[3])
        cut_legth_range = str(cut_legth_2)+"-"+str(cut_legth_1)
        Jacket_FE_1 = float(e[6])+float(e[8])
        Jacket_FE_2 = float(e[6])+float(e[7])
        Jacket_FE_range = str(Jacket_FE_2)+"-"+str(Jacket_FE_1)
        Jacket_TE_1 = float(e[9])+float(e[11])
        Jacket_TE_2 = float(e[9])+float(e[10])
        Jacket_TE_range = str(Jacket_TE_2)+"-"+str(Jacket_TE_1)
        mycursor.execute(
            "INSERT INTO FG_Cut_Details(FG_Part_Number,Component_Number,Cable_Sl,Description,Cut_Machine_id,cut_length,Jackeet_Machine_id,Jacket_FE,Jacket_TE)",
            (list_1[0], list_1[1], list_1[2], e[0], e[1], cut_legth_range, e[5], Jacket_FE_range, Jacket_TE_range))
        db.commmit()
# Entering FG Component Data
        for j, f in e[12]:
            FE_strip_1 = float(f[2])+float(f[4])
            FE_strip_2 = float(f[2])+float(f[3])
            FE_Strip_Range = str(FE_strip_2)+"-"+str(FE_strip_1)

            TE_Strip_1 = float(f[5])+float(f[7])
            TE_Strip_2 = float(f[5])+float(f[6])
            TE_Strip_Range = str(TE_Strip_2)+"-"+str(TE_Strip_1)
            mycursor.execute(
                "INSERT INTO FG_Component_Data(FG_Part_Number,Component_Number,Cable_Sl,Core_Wire_Color,Stripping_tool_id,FE_Strip,TE_Strip) VALUES(%s,%s,%s,%s,%s,%s,%s)", (list_1[0], list_1[1], list_1[2], f[0], f[1], FE_Strip_Range, TE_Strip_Range))
            db.commmit()
# Insert FG_Crimp_Details:
    for i, e in ENUMERATE(list_l[4]):
        FE_Crimp_Height_1 = float(e[4])+float(e[6])
        FE_Crimp_Height_2 = float(e[4])+float(e[5])
        FE_Crimp_Height_Range = str(FE_Crimp_Height_2)+"-"+str(FE_Crimp_Height_1)

        TE_Crimp_Height_1 = float(e[13])+float(e[15])
        TE_Crimp_Height_2 = float(e[13])+float(e[14])
        TE_Crimp_Height_Range = str(TE_Crimp_Height_2)+"-"+str(TE_Crimp_Height_1)

        mycursor.execute("INSERT INTO FG_Crimp_Details(FG_Part_Number,Component_Number,Cable_Sl,FE_Crimp_Type,FE_Marker_Details,FE_Crimping_Instructions,FE_Terminal_PN,FE_Crimp_Height,FE_Pull_Force,FE_Crimp_tool,TE_Crimp_Type,TE_Marker_Details,TE_Crimping_Instructions,TE_Terminal_PN,TE_Crimp_Height,TE_Pull_Force,TE_Crimp_tool) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                         (list_1[0], list_1[1], list_1[2], e[2], e[1], e[8], e[3], FE_Crimp_Height_Range, e[7], e[9], e[11], e[10], e[17], e[12], TE_Crimp_Height_Range, e[16], e[17]))
        db.commmit()
# Insert FG_Assembly:
     for k, v in list_l[5].items():
         for i,e in enumerate(v):
             for j in (1,len(i)+1):
                 mycursor.execute("INSERT INTO FG_Assembly(Process,FG_Part_Number,Component_Number,Cable_Sl,Core_Wire_Colors,Testing_Machine_Board_No) VALUES(%s)", (k,list_1[0], list_1[1], list_1[2],e[j],e[0]))
                 db.commmit()



def Validate_Machine_Tool_id(Machine_tool_id):
    mycursor.execute(
        "SELECT Operation_Type FROM Plant_Details WHERE Machine_tool_id=%s", Machine_tool_id)
    op_t= mycursor.fetchall()
    if op_t[0] != "":
        return True
    else:
        return False


def Component_Details_db(Component_Number):
    mycursor.execute(
        "SELECT Component_Number FROM Component_Details WHERE EXISTS (SELECT Component_Number FROM Component_Details WHERE Component_Number=%s)", (
            Component_Number,))
    value_me= mycursor.fetchall()
    if value_me[0] != "":
        mycursor.execute(
            "SELECT Cable_desc,Core_Wire_Color FROM Component_Details WHERE Component_Number=%s", (Component_Number,))
        color_db= mycursor.fetchall()
        print(color_db)
        db_color= []
        for i, e in enumerate(color_db):  # making a list of colors
            db_color.append(e[1])
        return_desc= [True, color_db[0][0], db_color]
        return return_desc
    else:
        return False


def Update_Email_ID_UD_db(list_of_details):
    mycursor.execute(
        "UPDATE User_Details SET Username=%s,Plant_ID=%s,Access_Level=%s WHERE Email_ID=%s", list_of_details)
    db.commit()

# Component_Details_db("sw218")
