
import mysql.connector
# from textblob import TextBlob

db = mysql.connector.connect(
    host="HOST_NAME",
    user="users",
    password="Password",
    database="db_name"
)
#
# db = mysql.connector.connect(
#     host="HOST_NUMBER",
#     user="users",
#     password="Password",
#     database="db_name"
# )
# mycursor.execute("Create DATABASE tr_db")
mycursor = db.cursor()

lis = ["FG_Part_Number", "Description", "Customer_name", "Special_Instruction_Cutting",
       "Special_Instruction_Crimping", "Special_Instruction_Assembly", "Drawing_Rev", "Date_and_Time"]


def db_RM(lis, dict):
    fg_pno = lis[0]
    lis.pop(0)
    new_list = tuple(lis)
    mycursor.execute("""UPDATE FG_Detail
    SET Description=%s, Customer_name=%s, Special_Instruction_Cutting=%s, Special_Instruction_Crimping=%s, Special_Instruction_Assembly=%s, Drawing_Rev=%s, Date_and_Time=%s
    WHERE FG_Part_Number=%s""", new_list)


def Component_availability_db(Component_Number):
    my_data = []
    # mycursor.execute("SELECT COUNT(*) FROM Component_Details")
    # count = mycursor.fetchall()
    # print(count)
    # for x in (0, len(count))
    mycursor.execute(
        "SELECT Cable_desc,Core_Colour FROM Component_Details WHERE Component_Number=%s", (Component_Number,))
    data = mycursor.fetchall()
    print(data)
    for i in (0, len(data)-1):
        my_data.append(list(data[i]))
    my_data.insert(0, "")
    print(my_data)


def fetch_UD():
    mycursor.execute("""SELECT Username,Email_ID,Plant_ID,Access_Level FROM User_Details""")
    details = mycursor.fetchall()
    print(details)


# x = ["d", "psswd", "id45", 1, "fg@email.com"]


def Add_UD(x):
    mycursor.execute(
        "INSERT INTO User_Details(Username, Password, Plant_ID, Access_Level, Email_ID) VALUES(%s,%s,%s,%s,%s)", x)
    db.commit()


def Modify_UD(x):
    mycursor.execute(
        "UPDATE User_Details SET Username=%s, Password=%s, Plant_ID=%s, Access_Level=%s WHERE Email_ID=%s", x)
    db.commit()


def Delete_UD(x):
    mycursor.execute("DELETE FROM User_Details WHERE Email_ID=%s", (x,))
    db.commit()


Delete_UD("fg@gmail.com")

def
