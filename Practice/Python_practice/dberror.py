import mysql.connector
from textblob import TextBlob

db = mysql.connector.connect(
    host="host_name",
    user="Users",
    password="Password",
    database="db_name"
)

mycursor = db.cursor()
# mycursor.execute("Create DATABASE tr_db")

# Q5 = 'CREATE TABLE Crimping(Component_Number VARCHAR(40),Cable_Sl_Number VARCHAR(40),FE_Marker_Details VARCHAR(40),FE_Marker_PN VARCHAR(40),FE_Terminal_PN VARCHAR(40),FE_Crimp_Details VARCHAR(40),FE_Marker_Length VARCHAR(40),FE_Crimp_Height VARCHAR(40),FE_Pull_Force VARCHAR(40),FE_Marker_Instruction VARCHAR(40),TE_Marker_Details VARCHAR(40),TE_Marker_PN VARCHAR(40),TE_Terminal_PN VARCHAR(40),TE_Crimp_Details VARCHAR(40),TE_Marker_Length VARCHAR(40),TE_Crimp_Height VARCHAR(40),TE_Pull_Force VARCHAR(40),TE_Marker_Instruction VARCHAR(40))'
#
# mycursor.execute(Q5)
# db.commit()

# mycursor.executemany(
#     "INSERT INTO User_Details(Username, Email_ID, Plant_ID, Access_Level, Password) VALUES(%s,%s,%s,%s,%s)", [("SP1022", "5", '1234', '1', "30"), ("SP1010", "3", '1234', '2', "3"), ("SP1017", "3", '1234', '3', "10")])
#
# db.commit()


def validate_user_db(username, password):
    mycursor.execute("SELECT * FROM User_Details WHERE Username=%s", (username,))
    details = mycursor.fetchall()
    if len(details) != 0 and password == details[0][4]:
        availability = True
        return print([availability, details[0][0], details[0][3]])
    else:
        availability = False
        return print([availability])


validate_user_db("SP1010", "3")
