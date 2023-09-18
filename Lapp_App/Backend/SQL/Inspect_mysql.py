import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Tech@218",
    database="LAPP_Database"
)
mycursor = db.cursor()
# mycursor.execute("Create DATABASE LAPP_Database")

Q1 = "CREATE TABLE Inspection_Table (Lapp_Part_Number VARCHAR(40), Ballon_Number VARCHAR(40), Spec_Details VARCHAR(40), LSL VARCHAR(40), USL VARCHAR(40), Instruments_Used VARCHAR(40))"
Q2 = "CREATE TABLE Purchase_Input (Lapp_Part_Number VARCHAR(40), Supplier_Part_Number VARCHAR(40), Supplier_Name VARCHAR(40), Purchase_Order VARCHAR(40), GRN_Number VARCHAR(40), Quantity_Batch VARCHAR(40))"
Q3 = "CREATE TABLE Plant_Details (Plant_ID VARCHAR(40), Operation_Type VARCHAR(40), Process_Type VARCHAR(40), Machine_Type VARCHAR(40), Machine_tool_Number VARCHAR(40))"
Q4 = "CREATE TABLE Cable_Cutting (Lapp_Part_Number VARCHAR(40), Drawing_Rev VARCHAR(40), Customer_Name VARCHAR(40), Cable_Sl_Number VARCHAR(40), Cable_part_Number VARCHAR(40), Specifications_Cable_Cut_Length VARCHAR(40), Jacket_removing_length_from VARCHAR(40), Jacket_removing_length_to VARCHAR(40), Strip_length_from VARCHAR(40), Strip_length_to VARCHAR(40), Cutting_Special_Instruction VARCHAR(40), Part_ID VARCHAR(40), Marker details VARCHAR(40))"
Q5 = "CREATE TABLE Crimping (Lapp_Part_Number VARCHAR(40), Drawing_Rev VARCHAR(40), Customer_Name VARCHAR(40), Cable_Description VARCHAR(40), Specifications_Cable_Cut_Length VARCHAR(40), FE_Marker_details VARCHAR(40), FE_Crimping_Specifications VARCHAR(40), FE_Terminal_Part_Number. VARCHAR(40), FE_Specification_Crimp_height VARCHAR(40), FE_Comments VARCHAR(40), TE_Marker_details VARCHAR(40), TE_Crimping_specifications VARCHAR(40), TE_Terminal_part_Number VARCHAR(40), TE_Specification_Crimp_height VARCHAR(40), TE_Comments VARCHAR(40), Crimp_Special_Instruction VARCHAR(40))"
Q6 = "CREATE TABLE Assembly (Lapp_Part_Number VARCHAR(40), Cable_part_Number VARCHAR(40), Cable_Sl_Number VARCHAR(40), Process VARCHAR(40))"
Q7 = "CREATE TABLE Master_BOM (Lapp_Part_Number VARCHAR(40), Object_Description_Assembly VARCHAR(40), Unit_of_Measure VARCHAR(40), Assembly_Indicator BOOL)"
Q8 = "CREATE TABLE User_Details (Username VARCHAR(40), Email_ID VARCHAR(40), Plant_ID VARCHAR(40), Access_Level VARCHAR(40), Password VARCHAR(40))"
Q9 = "CREATE TABLE Changes (Username VARCHAR(40), Date_and_Time VARCHAR(40), Access_Level VARCHAR(40), Parameter_Changed VARCHAR(40), Parameters VARCHAR(40), Old_Value VARCHAR(40), New_Value VARCHAR(40), Modification VARCHAR(40))"
Q10 = "CREATE TABLE Work_Order_Details (Work_Order_Number VARCHAR(40), LAPP_Part_Number VARCHAR(40), Material_Description VARCHAR(40), Order_Quantity_GMEIN VARCHAR(40), Delivered_Quantity_GMEIN VARCHAR(40))"
mycursor.execute(Q1)
mycursor.execute(Q2)
mycursor.execute(Q3)
mycursor.execute(Q4)
mycursor.execute(Q5)
mycursor.execute(Q6)
mycursor.execute(Q7)
mycursor.execute(Q8)
mycursor.execute(Q9)
mycursor.execute(Q10)
db.commit()
# def LIT_User_Input(Lapp_Part_Number,Ballon_number):
#     print('\nChoose the corresponding Numerical Value for Instrument Data')
#     Instrument_data={1:'V',2:'VC',3:'M',4:'MS',5:'CSA'}
#     for i in Instrument_data.keys():print(str(i)+' '+Instrument_data[i])
#     Instrument=Instrument_data[int(input('Value: '))]
#     if Instrument=='V':
#         Spec_Details=str(input('Specification: '))
#         LSL=''
#         USL=''
#     else:
#         Spec_Details=float(input('Specification: '))
#         Lower_Tolerance=float(input('Lower_Tolerance: -'))
#         Upper_Tolerance=float(input('Upper_Tolerance: +'))
#         LSL=str(Spec_Details-Lower_Tolerance)
#         USL=str(Spec_Details+Upper_Tolerance)
#         Spec_Details=str(Spec_Details)
#
#     return (Lapp_Part_Number,Ballon_number,Spec_Details,LSL,USL,Instrument)
#
# def LIT_Add_value_one(Lapp_part_number):
#     print("\nAdd details for the Value:")
#
#     c=db.cursor()
#     n=int(input("Enter no. of ballons: "))
#     for i in range(1,n+1):
#         print('\nFor Ballon Number',i,)
#         data_input=LIT_User_Input(Lapp_part_number,i)
#         c.execute("INSERT INTO Inspection_Table VALUES (%s,%s,%s,%s,%s,%s)",data_input)
#     db.commit()
#
# def LIT_Modify(Lapp_Part_Number):
#
#         c=db.cursor()
#         print('\nEnter Parameter you want to modify')
#         Available_parameters={1:'Lapp_Part_Number',2:'Ballon_Number',3:'Spec_Details',4:'Tolerance',5:'Instrument'}
#         for i in Available_parameters.keys():print(str(i)+' '+Available_parameters[i])
#         match int(input('Modify: ')):
#             case 1:
#                 r=input('New Value: ')
#                 c.execute("""UPDATE Inspection_Table SET Lapp_Part_Number=%s WHERE Lapp_Part_Number=%s""",(r,Lapp_Part_Number))
#             case 2:
#                 Ballon_number=input('Ballon number to Change: ')#Make sure that it does not match with already existing ballon number for same part number
#                 r=input('New Value: ')
#                 c.execute("""UPDATE Inspection_Table SET Ballon_Number=%s WHERE Lapp_Part_Number=%s AND Ballon_Number=%s""",(r,Lapp_Part_Number,Ballon_number))
#             case _:
#                 Ballon_number=input('Ballon number: ')
#                 data=LIT_User_Input(Lapp_Part_Number,Ballon_number)
#                 c.execute("""UPDATE Inspection_Table SET Spec_Details=%s WHERE Lapp_Part_Number=%s AND Ballon_Number=%s""",(data[2],Lapp_Part_Number,Ballon_number))
#                 c.execute("""UPDATE Inspection_Table SET LSL=%s WHERE Lapp_Part_Number=%s AND Ballon_Number=%s""",(data[3],Lapp_Part_Number,Ballon_number))
#                 c.execute("""UPDATE Inspection_Table SET USL=%s WHERE Lapp_Part_Number=%s AND Ballon_Number=%s""",(data[4],Lapp_Part_Number,Ballon_number))
#                 c.execute("""UPDATE Inspection_Table SET Instruments_Used=%s WHERE Lapp_Part_Number=%s AND Ballon_Number=%s""",(data[5],Lapp_Part_Number,Ballon_number))
#
#         db.commit()
#
#
# def LIT_Delete_data(Lapp_Part_Number):
#
#     cur=db.cursor()
#
#     Deletion_Type=int(input('\nEnter Type of deletion\n1: Entire Lapp Part Number\n2: Specific Component in Lapp Part Number\n'))
#     if Deletion_Type==2:
#         Ballon_Number=str(input('Ballon Number: '))
#         cur.execute(""" DELETE FROM Inspection_table WHERE Lapp_Part_Number=%s AND Ballon_Number=%s
#         """,(Lapp_Part_Number,Ballon_Number))
#         print('Lapp Part '+Ballon_Number+' from '+Lapp_Part_Number+' Deleted')
#     elif Deletion_Type==1:
#         cur.execute(""" DELETE FROM Inspection_table WHERE Lapp_Part_Number=%s
#         """,(Lapp_Part_Number,))
#         print('Lapp Part '+Lapp_Part_Number+' Deleted')
#
#     db.commit()
#
# def LIT_LAPP_Part_data():
#     while True:
#         Lapp_Part_number=input('\nEnter LAPP Part Number (This data is case sensitive): ')
#
#         cur=db.cursor()
#         cur.execute(""" SELECT * FROM Inspection_table WHERE Lapp_Part_Number=%s""",(Lapp_Part_number,))
#         Part_details=cur.fetchall()
#         print(Part_details)
#         if len(Part_details)==0:
#             print("""\nData not available. Do you want to add a new Part Number.""")
#             print("""If you think that this data was previously entered. Please recheck the LAPP Part number. """)
#             match int(input('1:For adding \n2:For Entering LAPP Part number again \nOption: ')):
#                 case 1:
#                     LIT_Add_value_one(Lapp_Part_number)
#                 case 2:
#                     continue#Can give error handling feature by showing all part number by making in input case insensitive.
#         else:
#             print('',Part_details[0][0],'',sep='\n')
#             for Ballon_part_details in Part_details:
#                 print(Ballon_part_details[1]+' '+Ballon_part_details[2]+' '+Ballon_part_details[3]+' '+Ballon_part_details[4]+' '+Ballon_part_details[5])
#             match int(input('\n1:Export details to Excel Inspection Report\n2:Modify data \n3:Delete Part Data \nOption: ')):
#                 case 1:
#                     print('Feature not yet Available')
#                 case 2:
#                     LIT_Modify(Lapp_Part_number)
#                 case 3:
#                     LIT_Delete_data(Lapp_Part_number)
#                     #Can give error handling feature by showing all part number by making in input case insensitive.
#
# LIT_LAPP_Part_data()
