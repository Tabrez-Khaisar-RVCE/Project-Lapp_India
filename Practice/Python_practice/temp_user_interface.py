import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Tech@218",
    database="tr_db"
)
mycursor = db.cursor()
Part_number = str(input('Part_number '))
Description = str(input('Description '))
Drawing_rev = str(input('Drawing_rev '))
customer = str(input('Customer '))
Cutting_inst = str(input('Cutting_instruction '))
crimping_inst = str(input('crimping_instruction '))
assembly_inst = str(input('assembly_instruction '))
Component_qty = int(input('Component_qty '))

mycursor.execute("""INSERT INTO Master_BOM (FG_Part_Number, Description, Customer,
Drawing_Rev,Special_Instruction_Cutting, Special_Instruction_Crimping,
Special_Instruction_Assembly) VALUES(%s,%s,%s,%s,%s,%s,%s)""", (Part_number, Description, customer, Drawing_rev,
                                                                Cutting_inst, crimping_inst, assembly_inst))
db.commit()
i = 1
while i <= Component_qty:
    i += 1
    print('\n Component Qty: ', i-1, '/', Component_qty)
    component_part_number = str(input('component_part_number '))
    component_num = int(input('component_numbers '))
    j = 1
    while j <= component_num:
        Cable_sl = str(input('\n Cable_sl '))
        Cable_desc = str(input('Cable_description '))
        qty = str(input('qty '))
        cut_tool = str(input('cut_tool '))
        cut_length = float(input('cut_length '))
        cut_length_minus = abs(float(input('cut_length - ')))
        cut_length_plus = abs(float(input('cut_length + ')))
        cut_length = str(str(cut_length-cut_length_minus)+' to '+str(cut_length+cut_length_minus))
        JACKET_TOOL = str(input('JACKET_TOOL '))
        Jacket_FE = str(input('Jacket_FE '))
        Jacket_TE = str(input('Jacket_TE '))
        Strip_Tool = str(input('Strip_Tool '))
        Strip_FE = str(input('Strip_FE '))
        Strip_TE = str(input('Strip_TE '))
        core_color = str(input('core_color '))
        crimping = str(input('Crimp available?(y/n)'))
        mycursor.execute("""INSERT INTO Cable_Cutting (component_part_number,Cable_sl,Cable_desc,cut_length,qty,cut_tool,JACKET_TOOL,Jacket_FE,Jacket_TE,Strip_Tool,Strip_FE,Strip_TE,core_color) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                         (component_part_number, Cable_sl, Cable_desc, cut_length, qty, cut_tool, JACKET_TOOL, Jacket_FE, Jacket_TE, Strip_Tool, Strip_FE, Strip_TE, core_color))
        db.commit()
        if crimping = 'y'

        j += 1
# print(Part_number, Description, customer, Drawing_rev,
#       Cutting_inst, crimping_inst, assembly_inst)
