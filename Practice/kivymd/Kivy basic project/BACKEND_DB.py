import mysql.connector
# from textblob import TextBlob

db = mysql.connector.connect(
    host="HOST_NUMBER",
    user="USER_ADMIN",
    password="Password",
    database="db_name"
)
mycursor = db.cursor()


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

def Enter_FG_Details(list):
    mycursor.execute(
        "INSERT INTO FG_Details(FG_Part_Number,Description,Customer_name,Special_Instruction_Cutting,Special_Instruction_Crimping,Special_Instruction_Assembly,Drawing_Rev) VALUES(%s,%s,%s,%s,%s,%s,%s)", list)
    db.commit()


def Modify_FG_Details(list_of_details):
    mycursor.execute(
        "UPDATE FG_Details SET Description=%s,Customer_name=%s,Special_Instruction_Cutting=%s,Special_Instruction_Crimping=%s,Special_Instruction_Assembly=%s,Drawing_Rev=%s WHERE FG_Part_Number=%s", list_of_details)
    db.commit()

def Retrieve_Mtool_details_show_db(Machine_tool_id):
    mycursor.execute("Select * FROM Plant_Details WHERE Machine_tool_id=%s", (Machine_tool_id,))
    content = mycursor.fetchall()
    return content[0]
