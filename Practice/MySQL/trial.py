import mysql.connector

db = mysql.connector.connect(
    host="HOST_NUMBER",
    user="users",
    passwd="Password",
    database="db_name"
)

# mycursor.execute("Create DATABASE tr_db")
mycursor = db.cursor()
Q0 = """CREATE TABLE Component_Details(Component_Number VARCHAR(40),Cable_sl VARCHAR(40),Wire_Size VARCHAR(40),Core_Colour VARCHAR(40),Cable_desc VARCHAR(40))"""
# Q1 = "CREATE TABLE Inspection_Table (FG_Part_Number VARCHAR(40),Ballon_Number VARCHAR(40),Specification_Details VARCHAR(40),LSL VARCHAR(40),USL VARCHAR(40),Instruments_Used VARCHAR(40),FOREIGN KEY(FG_Part_Number) REFERENCES Purchase_Input(FG_Part_Number))"
Q2 = "CREATE TABLE Purchase_Input (FG_Part_Number VARCHAR(40),Supplier_Part_Number VARCHAR(40),Supplier_Name VARCHAR(40),Purchase_Order VARCHAR(40),GRN_Number VARCHAR(40),Quantity_Batch VARCHAR(40),PRIMARY KEY(FG_Part_Number))"
# Q3 = "CREATE TABLE Plant_Details (Plant_ID VARCHAR(40),Operation_Type VARCHAR(40),Process_Type VARCHAR(40),Machine_Tool_Number VARCHAR(40))"

# Q4 = '''CREATE TABLE Cable_Cutting(component_part_number VARCHAR(40),
#                                  Cable_sl VARCHAR(40), Cable_desc VARCHAR(60), cut_length VARCHAR(84), qty VARCHAR(40),
#                                  cut_tool VARCHAR(40), JACKET_TOOL VARCHAR(40), Jacket_FE VARCHAR(40), Jacket_TE VARCHAR(40), Strip_Tool VARCHAR(40),
#                                  Strip_FE VARCHAR(40), Strip_TE VARCHAR(40), core_color VARCHAR(40))'''
# mycursor.execute("DROP TABLE Crimping")
# Q5 = 'CREATE TABLE Crimping (Component_Number VARCHAR(40),Cable_Sl_Number  VARCHAR(40),FE_Marker_Details VARCHAR(40),FE_Marker_PN VARCHAR(40),FE_Terminal_PN VARCHAR(40),FE_Crimp_Details VARCHAR(40),FE_Marker_Length VARCHAR(40),FE_Crimp_Height VARCHAR(40),FE_Pull_Force VARCHAR(40),FE_Marker_Instruction VARCHAR(40),TE_Marker_Details VARCHAR(40),TE_Marker_PN VARCHAR(40),TE_Terminal_PN VARCHAR(40),TE_Crimp_Details VARCHAR(40),TE_Marker_Length VARCHAR(40),TE_Crimp_Height VARCHAR(40),TE_Pull_Force VARCHAR(40),TE_Marker_Instruction VARCHAR(40), PRIMARY KEY(Component_Number, Cable_Sl_Number))'
# Q6 = "CREATE TABLE Assembly (Component_Number VARCHAR(40),Cable_Sl_Number VARCHAR(40),Process VARCHAR(40),Testing_Machine_Board_No VARCHAR(40),PRIMARY KEY(Component_Number, Cable_Sl_Number))"
# Q7 = "CREATE TABLE Master_BOM(FG_Part_Number VARCHAR(40), Description VARCHAR(60), Customer VARCHAR(40), Special_Instruction_Cutting VARCHAR(40), Special_Instruction_Assembly VARCHAR(40), Special_Instruction_Crimping VARCHAR(40), Drawing_Rev VARCHAR(40), Date_and_Time VARCHAR(40), Special_Instruction_Cutting VARCHAR(255), Special_Instruction_Crimping VARCHAR(255), Special_Instruction_Assembly VARCHAR(255))"
# Q8 = "CREATE TABLE User_Details(Username VARCHAR(40), Email_ID VARCHAR(40), Plant_ID VARCHAR(40), Access_Level VARCHAR(40), Password VARCHAR(40), PRIMARY KEY (Email_ID))"
# Q9 = "CREATE TABLE Changes (Username VARCHAR(40),Date VARCHAR(40),Time VARCHAR(40),Access_Level VARCHAR(40),Parameters VARCHAR(40),Previous_Value VARCHAR(40),Updated_Value VARCHAR(40))"
# Q10 = "CREATE TABLE Work_Order_Details (Work_Order_Number VARCHAR(40), FG_Part_Number VARCHAR(40), Material_Description VARCHAR(60), WO_Qty_Total INTEGER(40), WO_Qty_Remaining INTEGER(40))"
# Q11 = "CREATE TABLE Junction (FG_Part_Number VARCHAR(40),Component_Number VARCHAR(40),Cable_Sl_Number VARCHAR(40),PRIMARY KEY(FG_Part_Number))"
# mycursor.execute(
#     """ALTER TABLE Junction ADD CONSTRAINT fk3 FOREIGN KEY(Component_Number, Cable_Sl_Number) REFERENCES Assembly(Component_Number, Cable_Sl_Number)""")
# mycursor.execute("""ALTER TABLE Assembly DROP PRIMARY KEY,
#                     ADD PRIMARY KEY(Component_Number, Cable_Sl_Number)""")
# mycursor.execute(Q0)
# mycursor.execute(Q1)
# mycursor.execute(Q2)
# mycursor.execute(Q3)
# mycursor.execute(Q4)
# mycursor.execute(Q5)
# mycursor.execute(Q6)
# mycursor.execute(Q7)
# mycursor.execute(Q8)
# mycursor.execute(Q9)
# mycursor.execute(Q10)
# mycursor.execute(Q11)
# # #
# mycursor.executemany("INSERT INTO User_Details (Username, Email_ID, Plant_ID, Access_Level, Password) VALUES(%s,%s,%s,%s,%s)",
#                      [("Affn", "affanahmed2000@gmail.com", "6186", 3, 'Gadget'), ("Shiish", "shirishkumar.lapp@gmail.com", "6186", 3, 'Password.123'), ("Tbrez", "Tabrez.lapp@gmail.com", "6186", 3, 'Tabrez@Lapp'), ("Muzkkir", "Muzakkirjlapp@gmail.com", "6186", 3, 'Password.123')])
# # db.commit()
# Drop command
# storing wo table
# download report:
mycursor.execute("DROP EVENT tezt")
# mycursor.execute("SELECT * FROM Work_Order_Details")
# d = mycursor.fetchall()
mycursor.execute(
    "CREATE EVENT tezt ON SCHEDULE EVERY 1 MINUTE STARTS CURRENT_TIMESTAMP DO DELETE from Work_Order_Details WHERE WO_Qty_Delivered=%s", (0,))
db.commit()
# print(d)
# import mysql.connector


# def Edit(value_WO: str, value_qty: int):
#
#     mycursor.execute(
#         "SELECT  WO_Qty_Remaining FROM Work_Order_Details WHERE Work_Order_Number=%s", (value_WO,))
#     d = mycursor.fetchall()
#     print(d)
#     a = d[0][0]-value_qty
#     print(a)
#     mycursor.execute(
#         "UPDATE Work_Order_Details SET WO_Qty_Remaining=%s WHERE Work_Order_Number=%s", (a, value_WO))
#     db.commit()
#
#
# Edit('SP1021', 7)
# db = mysql.connector.connect(
#     host="HOST_NAME",
#     user="users",
#     passwd="Password"
#
# )
# mycursor = db.cursor()
# mycursor.execute("Create DATABASE SQLAlchemy ")
# def held_WO_SQL():
#     pass
#     SELECT Work_Order_Number FROM Work_Order_Details

# mycursor.execute("""SELECT Junction.*, cable_cutting.*
# FROM Junction
# LEFT JOIN cable_cutting
# ON cable_cutting.component_part_number = Junction.Component_Number
# """)
# d = mycursor.fetchall()
# print(d)

# mycursor.execute("INSERT INTO Junction(FG_Part_Number, Component_Number, Cable_Sl_Number) VALUES(%s,%s,%s)",
#                  ("Muzakkirjlapp@gmail.com", "3", "3"))
# mycursor.execute("INSERT INTO Master_BOM(FG_Part_Number, Description, Customer, Special_Instruction_Cutting, Special_Instruction_Assembly, Special_Instruction_Crimping, Drawing_Rev, Date_and_Time) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",
#                  ("3", "Muzakkir", "Muzakkirjlapp@gmail.com", "6186", "3", 'Password.123', "Muzakkir", "Muzakkirjlapp@gmail.com"))
# db.commit()
