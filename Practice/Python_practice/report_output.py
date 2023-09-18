from run_temp import report_output
from functions import Retrieve_terminal_backed_db

w=["FG 38062758","DESC R9579-38071-00 ME-GE 4 (1440-1536/70)", "NAME KTTM", "Special_Instructionnnn", "cutting specification", "crimping specification", "assembly specification", "A", "DateTime"]
x=[["COMPONENT NO.1234", "CABLE SNO.1", "ÖLFLEX®100 I1x0.50", "CUT TOOL A23456", "CUT LENGHT 26070 to 26090", "JACKET  #M T A1234", "JACKET FE 1 to 2", "JACKET TE 3 to 4", [["black", "1.5 to 1.8", "2.5 to 2.8", "STRIP TOOL A1"], ["blue", "3.5 to 3.8", "4.5 to 4.8", "STRIP TOOL A2"]]],
["COMPONENT NO.5678", "CABLE SNO.2", "ÖLFLEX®100 I2x0.50", "CUT TOOL A12345", "CUT LENGHT 45654 to 987654", "JACKET  #M T A9876", "JACKET FE 5 to 6", "JACKET TE 7 to 8", [["red", "5.5 to 5.8", "6.5 to 6.8", "STRIP TOOL A3"], ["green", "7.5 to 7.8", "8.5 to 8.8", "STRIP TOOL A4"]]]]
y=[["COMPONENT NO.5678", "CABLE SINO1", "CORE COLOR1","CRIMP FE MARKER PNO R4", "FE MARKER DETAILS SP0976", "FE CRIPM1", "1234", "FE CRIMP HEIGHT1", "FE PULL FORCE1", "FE CRIMP DETAILS1", "FE CRIMP TOOL1", "TE MARKER PNO SS", "TE MARKER DETAILS SP3455", "TE CRIPM1", "123445", "TE CRIMP HEIGHT1", "TE PULL FORCE1", "TE CRIMP DETAILS1", "TE CRIMP TOOL1"],
["COMPONENT NO.5678", "CABLE SINO2", "CORE COLOR2","CRIMP FE MARKER PNO YY", "FE MARKER DETAILS SP123", "FE CRIPM2", "1234567", "FE CRIMP HEIGHT2", "FE PULL FORCE2", "FE CRIMP DETAILS2", "FE CRIMP TOOL2", "TE MARKER PNO ZZ", "TE MARKER DETAILS SP9876", "TE CRIPM2", "1234455", "TE CRIMP HEIGHT2", "TE PULL FORCE2", "TE CRIMP DETAILS2", "TE CRIMP TOOL2"]]
z=[[["Connector housing Connector Assembly"],['wno1', 'pno1', 'tm1'],['wno2', 'pno2', 'tm2'], ['wno3', 'pno3', 'tm3']], [["Ink jet printing"],['wno4', 'pno4', 'tm4'],['wno5', 'pno5', 'tm5'], ['wno6', 'pno7', 'tm8']]]
# report_output(w,x,y,z)
crimp_component_number=[]
crimp_repreat=[]
cut_component_number=[]
cut_component_details=[]

for data in y:
    if not data[0] in crimp_component_number:
        crimp_component_number.append(data[0])
        crimp_repreat.append([data[0],1])
    else:
        crimp_repreat[crimp_component_number.index(data[0])][1]+=1

for data in x:
    cut_component_number.append(data[0])
    cut_component_details.append([data[4],data[6],data[7]])

for component_number_in_crimp in crimp_component_number:
    if component_number_in_crimp in cut_component_number:
        y[crimp_component_number.index(component_number_in_crimp)]+=cut_component_details[cut_component_number.index(component_number_in_crimp)]
        for i in range(crimp_repreat[crimp_component_number.index(data[0])][1]-1):
            y[crimp_component_number.index(component_number_in_crimp)+i+1]+=cut_component_details[cut_component_number.index(component_number_in_crimp)]

for position,details in enumerate(y):
    FE_terminal_strip=Retrieve_terminal_backed_db(details[6])
    TE_terminal_strip=Retrieve_terminal_backed_db(details[14])

    if FE_terminal_strip==[] or TE_terminal_strip==[]:
        print([False,'Terminal_error'])
        break

    y[position]+=[FE_terminal_strip[0][0],TE_terminal_strip[0][0]]



print(y)
