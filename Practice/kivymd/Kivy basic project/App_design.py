from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.factory import Factory
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.screenmanager import ScreenManager, Screen

class AddComponentPartNumber(Screen):
    Component_details=[]

    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def PNO(self):
        component_qty=self.parent.fgqty()
        self.ids.PartNumber.text=self.parent.pno1()
        self.ids.ComponentQTY_txt.text=str(component_qty[0]+1) +'/'+str(component_qty[1])

    def temp_function(self):
        if self.ids.ComponentPNO.text=='1234':
            return [True,'desc',['black 1','black 2','noodles','black 3','black 4','black 5','black 6','black 7','black 8','black 9','black 10','black 11','black 12','black 13','black 14']]
        elif self.ids.ComponentPNO.text=='12':
            return [True,'desc',['black 1','black 2','orange','black 3','black 4','black 5']]
        else:
            return [False]

    def validate_PNO(self):
        validation_Component= self.temp_function()
        # function_name(self.ids.ComponentPNO)
        if validation_Component[0]==False:
            return False
        else:
            self.Component_details=validation_Component[1:]
            return True

    def Component_details_values(self):
        return self.Component_details

    def validate_PNO_state(self):
        self.ids.err_label.text='Component Number is Not Available.'

class Tab_In(TabbedPanel):

    def __init__(self,**kwargs):
        super().__init__(**kwargs)

class Assembly_table_Input(BoxLayout):
    Component_data=[]
    Assembly_data={}

    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def CI_ASM_details(self,Core_data):
        Headings_CI_ASM=[]

        if not self.Component_data==[]:
            self.ids.err_label.text='Warning: Cores have been removed from Available Cores. However Cores are not removed from Core Wire colors.'

        for individual_data in Core_data:
            Headings_CI_ASM.append({'text':individual_data})

        self.ids.tablular_data_cores.data = Headings_CI_ASM

        self.Component_data=Core_data

        print(self.Component_data)

        if Core_data==[]: # change if core remove
            self.ids.tablular_data_assembly.data = []
            self.Assembly_data={}
            return



    def show_data_on_screen(self):
        Headings=[]

        for individual_data in self.Assembly_data:
            Headings.append({'text':individual_data})
            count=0
            for data_in_data in self.Assembly_data[individual_data]:
                count+=1
                if count>1:
                    Headings.append({'text':''})
                print(data_in_data)
                a=''
                for i in data_in_data[1:]:
                    a+=i+', '
                Headings.append({'text':a,'width':dp(300)})
                Headings.append({'text':data_in_data[0]})

        self.ids.tablular_data_assembly.data = Headings
        print(Headings)
        print(self.ids.tablular_data_assembly.data)

    def clear_screen(self):
        self.ids.ASM_CoreWireColor.text=''
        self.ids.ASM_Board.text=''
        self.ids.ASM_Group.text=''

    def add_assembly_data(self):

        if self.ids.ASM_CoreWireColor.text in self.Component_data:
            self.ids.err_label.text=''
            self.ids.ASM_CoreWireColor.background_color=(1,1,1,1)
        else:
            self.ids.err_label.text='Core Wire not available.'
            self.ids.ASM_CoreWireColor.background_color=(1,0,0,0.8)
            return

        if self.ids.ASM_Process.text in self.Assembly_data.keys():
            if self.ids.ASM_Group.text=='' or self.ids.ASM_Group.text=='-' or self.ids.ASM_Group.text=='0':
                if not self.ids.ASM_Board.text in ['1','2']:
                    self.ids.ASM_Board.background_color=(1,0,0,0.8)
                    self.ids.err_label.text= 'Testing Machine/Board ID not available. '
                    return
                else:
                    self.ids.ASM_Board.background_color=(1,1,1,1)

                self.Assembly_data[self.ids.ASM_Process.text].append([self.ids.ASM_Board.text, self.ids.ASM_CoreWireColor.text])
            else:
                try:
                    self.Assembly_data[self.ids.ASM_Process.text][int(self.ids.ASM_Group.text)-1].append(self.ids.ASM_CoreWireColor.text)
                except IndexError:
                    self.ids.err_label.text= 'Group does not exist'
        else:
            if not self.ids.ASM_Board.text in ['1','2']:
                self.ids.ASM_Board.background_color=(1,0,0,0.8)
                self.ids.err_label.text= 'Testing Machine/Board ID not available. '
                return
            else:
                self.ids.ASM_Board.background_color=(1,1,1,1)
            self.Assembly_data[self.ids.ASM_Process.text]=[[self.ids.ASM_Board.text, self.ids.ASM_CoreWireColor.text]]

        print(self.Assembly_data)
        self.show_data_on_screen()
        self.clear_screen()

    def remove_assembly_data(self):
        if self.ids.ASM_Group.text =='' or self.ids.ASM_Group.text=='-' or self.ids.ASM_Group.text=='0':
            try:
                del self.Assembly_data[self.ids.ASM_Process.text]
                self.show_data_on_screen()
            except:
                self.ids.err_label.text= 'Process does not exist'
        else:
            try:
                del self.Assembly_data[self.ids.ASM_Process.text][int(self.ids.ASM_Group.text)-1]
                if self.Assembly_data[self.ids.ASM_Process.text]==[]:del self.Assembly_data[self.ids.ASM_Process.text]
                self.show_data_on_screen()
            except:
                self.ids.err_label.text= 'Group does not exist.'


class Crimping_table_Input(BoxLayout):
    Crimp_list_Core=[]
    Component_data=[]

    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def CI_CRI_Info(self,Crimp_Core):
        Headings=[]
        modified_Crimp_list_Core=[]
        modified_Component_data=[]

        for index,individual_data in enumerate(Crimp_Core):
            modified_Component_data.append(individual_data)

            if individual_data in self.Component_data:
                modified_Crimp_list_Core.append(self.Crimp_list_Core[self.Component_data.index(individual_data)])

                for i,j in enumerate(self.Crimp_list_Core[self.Component_data.index(individual_data)]):
                    if i==8 or i==17:
                        Headings.append({'text':j,'size_hint_x':None,'width':dp(150)})
                    else:
                        Headings.append({'text':j})
                continue

            else:
                Headings.append({'text':individual_data})
                core_list=[individual_data]

                for j in range(18):
                    if j==7 or j==16:
                        Headings.append({'text':'','size_hint_x':None,'width':dp(150)})
                    else:
                        Headings.append({'text':''})
                    core_list.append('')

                modified_Crimp_list_Core.append(core_list)

        self.Crimp_list_Core=modified_Crimp_list_Core
        self.Component_data=modified_Component_data

        self.ids.tablular_data.data = Headings

    def show_data_on_screen(self):
        self.Headings=[]

        for individual_data in self.Crimp_list_Core:
            if individual_data[2]=='':
                self.Headings.append({'text':individual_data[0]})
                for j in range(18):
                    if j==7 or j==16:
                        self.Headings.append({'text':'','size_hint_x':None,'width':dp(150)})
                    else:
                        self.Headings.append({'text':''})
            else:
                for i,j in enumerate(individual_data):
                    if i==8 or i==17:
                        self.Headings.append({'text':j,'size_hint_x':None,'width':dp(150)})
                    else:
                        self.Headings.append({'text':j})

        self.ids.tablular_data.data = self.Headings
        print(self.Crimp_list_Core)

    def clear_screen(self):
        self.ids.CRI_FE_MarkerDetails_PNO.text=''
        self.ids.CRI_FE_CrimpType.text=''
        self.ids.CRI_FE_TreminalPNO.text=''
        self.ids.CRI_FE_CrimpHeight.text=''
        self.ids.CRI_FE_CrimpHeightMin.text=''
        self.ids.CRI_FE_CrimpHeightPlus.text=''
        self.ids.CRI_FE_PullForce.text=''
        self.ids.CRI_FE_CrimpInstruction.text=''
        self.ids.CRI_FE_CrimpTool.text=''
        self.ids.CRI_TE_MarkerDetails_PNO.text=''
        self.ids.CRI_TE_CrimpType.text=''
        self.ids.CRI_TE_TreminalPNO.text=''
        self.ids.CRI_TE_CrimpHeight.text=''
        self.ids.CRI_TE_CrimpHeightMin.text=''
        self.ids.CRI_TE_CrimpHeightPlus.text=''
        self.ids.CRI_TE_PullForce.text=''
        self.ids.CRI_TE_CrimpInstruction.text=''
        self.ids.CRI_TE_CrimpTool.text=''

    def remove_color(self):
        self.ids.CRI_FE_MarkerDetails_PNO.background_color=(1,1,1,1)
        self.ids.CRI_FE_MarkerDetails_PNO.background_color=(1,1,1,1)
        self.ids.CRI_FE_CrimpType.background_color=(1,1,1,1)
        self.ids.CRI_FE_TreminalPNO.background_color=(1,1,1,1)
        self.ids.CRI_FE_CrimpHeight.background_color=(1,1,1,1)
        self.ids.CRI_FE_CrimpHeightMin.background_color=(1,1,1,1)
        self.ids.CRI_FE_CrimpHeightPlus.background_color=(1,1,1,1)
        self.ids.CRI_FE_PullForce.background_color=(1,1,1,1)
        self.ids.CRI_FE_CrimpInstruction.background_color=(1,1,1,1)
        self.ids.CRI_FE_CrimpTool.background_color=(1,1,1,1)
        self.ids.CRI_TE_MarkerDetails_PNO.background_color=(1,1,1,1)
        self.ids.CRI_TE_CrimpType.background_color=(1,1,1,1)
        self.ids.CRI_TE_TreminalPNO.background_color=(1,1,1,1)
        self.ids.CRI_TE_CrimpHeight.background_color=(1,1,1,1)
        self.ids.CRI_TE_CrimpHeightMin.background_color=(1,1,1,1)
        self.ids.CRI_TE_CrimpHeightPlus.background_color=(1,1,1,1)
        self.ids.CRI_TE_PullForce.background_color=(1,1,1,1)
        self.ids.CRI_TE_CrimpInstruction.background_color=(1,1,1,1)
        self.ids.CRI_TE_CrimpTool.background_color=(1,1,1,1)


    def call_list_Crimp(self):
        self.ids.err_label.text=''

        err_MissingInfo=False

        if self.ids.CRI_FE_MarkerDetails_PNO.text == '':
            err_MissingInfo=True
            self.ids.err_label.text+= 'FE Marker details and PN, '
            self.ids.CRI_FE_MarkerDetails_PNO.background_color=(1,0,0,0.8)
        else:
            self.ids.CRI_FE_MarkerDetails_PNO.background_color=(1,1,1,1)

        if self.ids.CRI_TE_MarkerDetails_PNO.text == '' :
            err_MissingInfo=True
            self.ids.err_label.text+= 'TE Marker details and PN, '
            self.ids.CRI_TE_MarkerDetails_PNO.background_color=(1,0,0,0.8)
        else:
            self.ids.CRI_TE_MarkerDetails_PNO.background_color=(1,1,1,1)

        if self.ids.CRI_FE_CrimpType.text == '':
            err_MissingInfo=True
            self.ids.err_label.text+= 'FE Crimp Type, '
            self.ids.CRI_FE_CrimpType.background_color=(1,0,0,0.8)
        else:
            self.ids.CRI_FE_CrimpType.background_color=(1,1,1,1)

        if self.ids.CRI_TE_CrimpType.text == '':
            err_MissingInfo=True
            self.ids.err_label.text+= 'TE Crimp Type, '
            self.ids.CRI_TE_CrimpType.background_color=(1,0,0,0.8)
        else:
            self.ids.CRI_TE_CrimpType.background_color=(1,1,1,1)

        if self.ids.CRI_FE_CrimpInstruction.text == '':
            err_MissingInfo=True
            self.ids.err_label.text+= 'FE Crimping Instruction, '
            self.ids.CRI_FE_CrimpInstruction.background_color=(1,0,0,0.8)
        else:
            self.ids.CRI_FE_CrimpInstruction.background_color=(1,1,1,1)

        if self.ids.CRI_TE_CrimpInstruction.text == '':
            err_MissingInfo=True
            self.ids.err_label.text+= 'TE Crimping Instruction, '
            self.ids.CRI_TE_CrimpInstruction.background_color=(1,0,0,0.8)
        else:
            self.ids.CRI_TE_CrimpInstruction.background_color=(1,1,1,1)

        if err_MissingInfo==True:
            self.ids.err_label.text+= 'is empty.'
            return None


        if self.ids.CRI_FE_CrimpHeight.text=='' or self.ids.CRI_FE_CrimpHeight.text=='-': self.ids.CRI_FE_CrimpHeight.text='0'
        if self.ids.CRI_FE_CrimpHeightMin.text==''or self.ids.CRI_FE_CrimpHeightMin.text=='-': self.ids.CRI_FE_CrimpHeightMin.text='0'
        if self.ids.CRI_FE_CrimpHeightPlus.text==''or self.ids.CRI_FE_CrimpHeightPlus.text=='-':self.ids.CRI_FE_CrimpHeightPlus.text='0'
        if self.ids.CRI_FE_PullForce.text==''or self.ids.CRI_FE_PullForce.text=='-':self.ids.CRI_FE_PullForce.text='0'
        if self.ids.CRI_TE_CrimpHeight.text==''or self.ids.CRI_TE_CrimpHeight.text=='-':self.ids.CRI_TE_CrimpHeight.text='0'
        if self.ids.CRI_TE_CrimpHeightMin.text==''or self.ids.CRI_TE_CrimpHeightMin.text=='-':self.ids.CRI_TE_CrimpHeightMin.text='0'
        if self.ids.CRI_TE_CrimpHeightPlus.text==''or self.ids.CRI_TE_CrimpHeightPlus.text=='-':self.ids.CRI_TE_CrimpHeightPlus.text='0'
        if self.ids.CRI_TE_PullForce.text==''or self.ids.CRI_TE_PullForce.text=='-':self.ids.CRI_TE_PullForce.text='0'

        err_calc=False

        Crimp_FE_TolMin=float(self.ids.CRI_FE_CrimpHeight.text)-float(self.ids.CRI_FE_CrimpHeightMin.text)
        Crimp_TE_TolMin=float(self.ids.CRI_TE_CrimpHeight.text)-float(self.ids.CRI_TE_CrimpHeightMin.text)

        if Crimp_FE_TolMin<0: #<=
            err_calc=True
            self.ids.err_label.text= 'Cut length, '
            self.ids.CRI_FE_CrimpHeight.background_color=(1,0,0,0.8)
        else:
            self.ids.CRI_FE_CrimpHeight.background_color=(1,1,1,1)

        if Crimp_TE_TolMin<0: #<=
            err_calc=True
            self.ids.err_label.text+= 'Jacket remove FE length, '
            self.ids.CRI_TE_CrimpHeight.background_color=(1,0,0,0.8)
        else:
            self.ids.CRI_TE_CrimpHeight.background_color=(1,1,1,1)

        if err_calc==True:
            self.ids.err_label.text+= ' -ve or 0.'
            return None

        err_tool_terminal=False

        if not self.ids.CRI_FE_CrimpTool.text in ['1','2']:
            err_tool_terminal=True
            self.ids.CRI_FE_CrimpTool.background_color=(1,0,0,0.8)
            self.ids.err_label.text= 'FE Crimp Tool, '
        else:
            self.ids.CRI_FE_CrimpTool.background_color=(1,1,1,1)
            # CrimpToolDetails_db(plant_id)

        if not self.ids.CRI_TE_CrimpTool.text in ['1','2']:
            err_tool_terminal=True
            self.ids.CRI_TE_CrimpTool.background_color=(1,0,0,0.8)
            self.ids.err_label.text= 'TE Crimp Tool, '
        else:
            self.ids.CRI_TE_CrimpTool.background_color=(1,1,1,1)
            # CrimpToolDetails_db(plant_id)

        if not self.ids.CRI_FE_TreminalPNO.text in ['1','2']:
            err_tool_terminal=True
            self.ids.CRI_FE_TreminalPNO.background_color=(1,0,0,0.8)
            self.ids.err_label.text= 'FE Treminal PNO, '
        else:
            self.ids.CRI_FE_TreminalPNO.background_color=(1,1,1,1)

        if not self.ids.CRI_TE_TreminalPNO.text in ['1','2']:
            err_tool_terminal=True
            self.ids.CRI_TE_TreminalPNO.background_color=(1,0,0,0.8)
            self.ids.err_label.text= 'TE Treminal PNO, '
        else:
            self.ids.CRI_TE_TreminalPNO.background_color=(1,1,1,1)

        if err_tool_terminal==True:
            self.ids.err_label.text+= 'not available in the Database.'
            return None

        return [self.ids.CRI_CoreWireColor.text,self.ids.CRI_FE_MarkerDetails_PNO.text, self.ids.CRI_FE_CrimpType.text, self.ids.CRI_FE_TreminalPNO.text, self.ids.CRI_FE_CrimpHeight.text,
        self.ids.CRI_FE_CrimpHeightMin.text,self.ids.CRI_FE_CrimpHeightPlus.text, self.ids.CRI_FE_PullForce.text,self.ids.CRI_FE_CrimpInstruction.text,
        self.ids.CRI_FE_CrimpTool.text, self.ids.CRI_TE_MarkerDetails_PNO.text, self.ids.CRI_TE_CrimpType.text, self.ids.CRI_TE_TreminalPNO.text,
        self.ids.CRI_TE_CrimpHeight.text,self.ids.CRI_TE_CrimpHeightMin.text,self.ids.CRI_TE_CrimpHeightPlus.text,self.ids.CRI_TE_PullForce.text,
        self.ids.CRI_TE_CrimpInstruction.text,self.ids.CRI_TE_CrimpTool.text]

    def retrieve_crimping_data(self):
        self.ids.err_label.text= ''

        if self.ids.CRI_CoreWireColor.text=='':
            for i in self.Crimp_list_Core:
                if i[2]=='':
                    self.ids.CRI_CoreWireColor.text=i[0]
                    self.clear_screen()
                    self.remove_color()
                    return
            self.ids.err_label.text='Core Wire is Empty.'
            return

        CC_check=[]
        for core_data in self.Crimp_list_Core:
            CC_check.append(core_data[0])

        if self.ids.CRI_CoreWireColor.text in CC_check:
            retrieve_index=CC_check.index(self.ids.CRI_CoreWireColor.text)
            print(retrieve_index)

            if self.Crimp_list_Core[retrieve_index][2]=='':
                self.clear_screen()
                self.remove_color()
                return
            else:
                self.ids.CRI_FE_MarkerDetails_PNO.text=self.Crimp_list_Core[retrieve_index][1]
                self.ids.CRI_FE_CrimpType.text=self.Crimp_list_Core[retrieve_index][2]
                self.ids.CRI_FE_TreminalPNO.text=self.Crimp_list_Core[retrieve_index][3]
                self.ids.CRI_FE_CrimpHeight.text=self.Crimp_list_Core[retrieve_index][4]
                self.ids.CRI_FE_CrimpHeightMin.text=self.Crimp_list_Core[retrieve_index][5]
                self.ids.CRI_FE_CrimpHeightPlus.text=self.Crimp_list_Core[retrieve_index][6]
                self.ids.CRI_FE_PullForce.text=self.Crimp_list_Core[retrieve_index][7]
                self.ids.CRI_FE_CrimpInstruction.text=self.Crimp_list_Core[retrieve_index][8]
                self.ids.CRI_FE_CrimpTool.text=self.Crimp_list_Core[retrieve_index][9]
                self.ids.CRI_TE_MarkerDetails_PNO.text=self.Crimp_list_Core[retrieve_index][10]
                self.ids.CRI_TE_CrimpType.text=self.Crimp_list_Core[retrieve_index][11]
                self.ids.CRI_TE_TreminalPNO.text=self.Crimp_list_Core[retrieve_index][12]
                self.ids.CRI_TE_CrimpHeight.text=self.Crimp_list_Core[retrieve_index][13]
                self.ids.CRI_TE_CrimpHeightMin.text=self.Crimp_list_Core[retrieve_index][14]
                self.ids.CRI_TE_CrimpHeightPlus.text=self.Crimp_list_Core[retrieve_index][15]
                self.ids.CRI_TE_PullForce.text=self.Crimp_list_Core[retrieve_index][16]
                self.ids.CRI_TE_CrimpInstruction.text=self.Crimp_list_Core[retrieve_index][17]
                self.ids.CRI_TE_CrimpTool.text=self.Crimp_list_Core[retrieve_index][18]
                self.remove_color()

        else:
            self.ids.err_label.text= 'Core is not available'

    def modify_crimping_data(self):
        self.ids.err_label.text= ''

        CC_check=[]
        for core_data in self.Crimp_list_Core:
            CC_check.append(core_data[0])

        if self.ids.CRI_CoreWireColor.text in CC_check:
            Crimp_list=self.call_list_Crimp()

            if not Crimp_list == None:
                modify_index=CC_check.index(self.ids.CRI_CoreWireColor.text)
                self.Crimp_list_Core[modify_index]=Crimp_list
                self.show_data_on_screen()

                try:
                    if self.Crimp_list_Core[modify_index+1][2]=='':
                        self.ids.CRI_CoreWireColor.text=self.Crimp_list_Core[modify_index+1][0]
                        self.clear_screen()
                        self.ids.CRI_FE_MarkerDetails_PNO.focus=True
                    else:
                        self.ids.CRI_CoreWireColor.text=''
                        self.clear_screen()

                except IndexError:
                    self.ids.CRI_CoreWireColor.text=''
                    self.clear_screen()


        elif self.ids.CRI_CoreWireColor.text=='':
            self.ids.err_label.text= 'Core is empty'
            self.clear_screen()
        else:
            self.ids.err_label.text= 'Core is not available'
            self.clear_screen()

class Cutting_table_Input(BoxLayout):
    Cut_list_Com=[]
    Cut_list_Core=[]

    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def Comp_CI(self,Cut_Core_data):
        Headings=[]
        self.Cut_list_Com=[]

        self.ids.Show_Cable_desc.text=''
        self.ids.Show_Cut_MachineTool.text=''
        self.ids.Show_Cut_length.text=''
        self.ids.Show_Cut_TolMin.text=''
        self.ids.Show_Cut_TolPlus.text=''
        self.ids.Show_Jacket_MachineTool.text=''
        self.ids.Show_Jacket_FE.text=''
        self.ids.Show_Jacket_FE_TolMin.text=''
        self.ids.Show_Jacket_FE_TolPlus.text=''
        self.ids.Show_Jacket_TE.text=''
        self.ids.Show_Jacket_TE_TolMin.text=''
        self.ids.Show_Jacket_TE_TolPlus.text=''

        self.ids.CI_CableDesc.text=Cut_Core_data[0]
        self.ids.CI_CableDesc.disabled=True
        self.ids.Show_Cable_desc.text=self.ids.CI_CableDesc.text
        self.Cut_list_Core=Cut_Core_data[1]


        for index,individual_data in enumerate(self.Cut_list_Core):
            Headings.append({'text':individual_data})
            core_list=[individual_data]
            for j in range(9):
                Headings.append({'text':''})
                core_list.append('')
            self.Cut_list_Core[index]=core_list

        print(self.Cut_list_Com,self.Cut_list_Core)

        self.ids.tablular_data.data = Headings

    def CI_ASM_Data_Sending(self):
        ASM_Cores=[]
        for Core_Details in self.Cut_list_Core:
            if Core_Details[9]==True:
                ASM_Cores.append(Core_Details[0])

        return ASM_Cores

    def CI_CRI_Data_Sending(self):
        CRI_Cores=[]
        for Core_Details in self.Cut_list_Core:
            if Core_Details[8]==True:
                CRI_Cores.append(Core_Details[0])

        return CRI_Cores

    def Show_Data_on_Screen(self):
        self.Headings=[]

        for Core_Details in self.Cut_list_Core:
            if Core_Details[2]=='':
                self.Headings.append({'text':Core_Details[0]})
                for j in range(9):
                    self.Headings.append({'text':''})
            else:
                for individual_data in Core_Details:
                    if type(individual_data)==str:
                        self.Headings.append({'text':individual_data})
                    else:
                        if individual_data==True:
                            self.Headings.append({'text':'Required'})
                        elif individual_data==False:
                            self.Headings.append({'text':''})

        self.ids.tablular_data.data = self.Headings
        print(self.Headings)

    def Show_Cable_Data_on_Screen(self):
        self.ids.Show_Cable_desc.text=self.Cut_list_Com[0]
        self.ids.Show_Cut_MachineTool.text=self.Cut_list_Com[1]
        self.ids.Show_Cut_length.text=self.Cut_list_Com[2]
        self.ids.Show_Cut_TolMin.text=self.Cut_list_Com[3]
        self.ids.Show_Cut_TolPlus.text=self.Cut_list_Com[4]
        self.ids.Show_Jacket_MachineTool.text=self.Cut_list_Com[5]
        self.ids.Show_Jacket_FE.text=self.Cut_list_Com[6]
        self.ids.Show_Jacket_FE_TolMin.text=self.Cut_list_Com[7]
        self.ids.Show_Jacket_FE_TolPlus.text=self.Cut_list_Com[8]
        self.ids.Show_Jacket_TE.text=self.Cut_list_Com[9]
        self.ids.Show_Jacket_TE_TolMin.text=self.Cut_list_Com[10]
        self.ids.Show_Jacket_TE_TolPlus.text=self.Cut_list_Com[11]

    def clear_screen(self):
        self.ids.CI_StripTool.text=''
        self.ids.CI_SFE.text=''
        self.ids.CI_SFE_TOLMin.text=''
        self.ids.CI_SFE_TOLPlus.text=''
        self.ids.CI_STE.text=''
        self.ids.CI_STE_TOLMin.text=''
        self.ids.CI_STE_TOLPlus.text=''
        self.ids.CI_CrI.active=False
        self.ids.CI_ASM.active=False

    def clear_color(self):
        self.ids.CI_StripTool.background_color=(1,1,1,1)
        self.ids.CI_SFE.background_color=(1,1,1,1)
        self.ids.CI_SFE_TOLMin.background_color=(1,1,1,1)
        self.ids.CI_SFE_TOLPlus.background_color=(1,1,1,1)
        self.ids.CI_STE.background_color=(1,1,1,1)
        self.ids.CI_STE_TOLMin.background_color=(1,1,1,1)
        self.ids.CI_STE_TOLPlus.background_color=(1,1,1,1)

    def call_list_Cable(self):

        self.ids.err_label.text=''

        if self.ids.CI_CableDesc.text == '':
            self.ids.err_label.text+= 'Cable Description, is empty.'
            self.ids.CI_CableDesc.background_color=(1,0,0,0.8)
        else:
            self.ids.CI_CableDesc.background_color=(1,1,1,1)


        if self.ids.CI_Cut.text=='' or self.ids.CI_Cut.text=='-': self.ids.CI_Cut.text='0'
        if self.ids.CI_Cut_TOLMin.text==''or self.ids.CI_Cut_TOLMin.text=='-': self.ids.CI_Cut_TOLMin.text='0'
        if self.ids.CI_Cut_TOLPlus.text==''or self.ids.CI_Cut_TOLPlus.text=='-':self.ids.CI_Cut_TOLPlus.text='0'
        if self.ids.CI_JFE.text==''or self.ids.CI_JFE.text=='-':self.ids.CI_JFE.text='0'
        if self.ids.CI_JFE_TOLMin.text==''or self.ids.CI_JFE_TOLMin.text=='-':self.ids.CI_JFE_TOLMin.text='0'
        if self.ids.CI_JFE_TOLPlus.text==''or self.ids.CI_JFE_TOLPlus.text=='-':self.ids.CI_JFE_TOLPlus.text='0'
        if self.ids.CI_JTE.text==''or self.ids.CI_JTE.text=='-':self.ids.CI_JTE.text='0'
        if self.ids.CI_JTE_TOLMin.text==''or self.ids.CI_JTE_TOLMin.text=='-':self.ids.CI_JTE_TOLMin.text='0'
        if self.ids.CI_JTE_TOLPlus.text==''or self.ids.CI_JTE_TOLPlus.text=='-':self.ids.CI_JTE_TOLPlus.text='0'

        err_calc=False

        Cut_length_TolMin=float(self.ids.CI_Cut.text)-float(self.ids.CI_Cut_TOLMin.text)
        Jacket_FE_TolMin=float(self.ids.CI_JFE.text)-float(self.ids.CI_JFE_TOLMin.text)
        Jacket_TE_TolMin=float(self.ids.CI_JTE.text)-float(self.ids.CI_JTE_TOLMin.text)

        if Cut_length_TolMin<=0:
            err_calc=True
            self.ids.err_label.text= 'Cut length, '
            self.ids.CI_Cut.background_color=(1,0,0,0.8)
        else:
            self.ids.CI_Cut.background_color=(1,1,1,1)

        if Jacket_FE_TolMin<0:
            err_calc=True
            self.ids.err_label.text+= 'Jacket remove FE length, '
            self.ids.CI_JFE.background_color=(1,0,0,0.8)
        else:
            self.ids.CI_JFE.background_color=(1,1,1,1)

        if Jacket_TE_TolMin<0:
            err_calc=True
            self.ids.err_label.text+= 'Jacket remove TE length, '
            self.ids.CI_JTE.background_color=(1,0,0,0.8)
        else:
            self.ids.CI_JTE.background_color=(1,1,1,1)

        if err_calc==True:
            self.ids.err_label.text+= ' -ve or 0.'
            return None

        err_tool=False

        if not self.ids.CI_CutTool.text in ['1','2']:
            err_tool=True
            self.ids.err_label.text+= 'Cut Tool, '
            self.ids.CI_CutTool.background_color=(1,0,0,0.8)
        else:
            self.ids.CI_CutTool.background_color=(1,1,1,1)
            # CutToolDetails_db(plant_id)
        if not self.ids.CI_JacketTool.text in ['2','3','NA']:
            err_tool=True
            self.ids.CI_JacketTool.background_color=(1,0,0,0.8)
            self.ids.err_label.text+= 'Jacket Tool, '
        else:
            self.ids.CI_JacketTool.background_color=(1,1,1,1)
            # JacketToolDetails_db(plant_id)
        if err_tool==True:
            self.ids.err_label.text+= 'not available in the Database.'
            return None

        self.Cut_list_Com=[self.ids.CI_CableDesc.text, self.ids.CI_CutTool.text, self.ids.CI_Cut.text, self.ids.CI_Cut_TOLMin.text,
        self.ids.CI_Cut_TOLPlus.text,self.ids.CI_JacketTool.text, self.ids.CI_JFE.text,self.ids.CI_JFE_TOLMin.text,
        self.ids.CI_JFE_TOLPlus.text, self.ids.CI_JTE.text, self.ids.CI_JTE_TOLMin.text, self.ids.CI_JTE_TOLPlus.text]

        self.Show_Cable_Data_on_Screen()


    def call_list_core(self):
        self.ids.err_label.text=''

        if self.ids.CI_SFE.text==''or self.ids.CI_SFE.text=='-':self.ids.CI_SFE.text='0'
        if self.ids.CI_SFE_TOLMin.text==''or self.ids.CI_SFE_TOLMin.text=='-':self.ids.CI_SFE_TOLMin.text='0'
        if self.ids.CI_SFE_TOLPlus.text==''or self.ids.CI_SFE_TOLPlus.text=='-':self.ids.CI_SFE_TOLPlus.text='0'
        if self.ids.CI_STE.text==''or self.ids.CI_STE.text=='-':self.ids.CI_STE.text='0'
        if self.ids.CI_STE_TOLMin.text==''or self.ids.CI_STE_TOLMin.text=='-':self.ids.CI_STE_TOLMin.text='0'
        if self.ids.CI_STE_TOLPlus.text==''or self.ids.CI_STE_TOLPlus.text=='-':self.ids.CI_STE_TOLPlus.text='0'

        Strip_FE_TolMin=float(self.ids.CI_SFE.text)-float(self.ids.CI_SFE_TOLMin.text)
        Strip_TE_TolMin=float(self.ids.CI_STE.text)-float(self.ids.CI_STE_TOLMin.text)

        err_calc=False

        if Strip_FE_TolMin<0:
            err_calc=True
            self.ids.err_label.text+= 'Strip remove FE length, '
            self.ids.CI_SFE.background_color=(1,0,0,0.8)
        else:
            self.ids.CI_SFE.background_color=(1,1,1,1)

        if Strip_TE_TolMin<0:
            err_calc=True
            self.ids.err_label.text+= 'Strip remove TE length, '
            self.ids.CI_STE.background_color=(1,0,0,0.8)
        else:
            self.ids.CI_STE.background_color=(1,1,1,1)

        if err_calc==True:
            self.ids.err_label.text+= ' -ve or 0.'
            return None

        if not self.ids.CI_StripTool.text in ['3','4']:
            self.ids.CI_StripTool.background_color=(1,0,0,0.8)
            self.ids.err_label.text+= 'Strip Tool, not available in the Database.'
            return None
        else:
            self.ids.CI_StripTool.background_color=(1,1,1,1)
            # StripToolDetails_db(plant_id)

        return [ self.ids.CI_CoreWireColor.text, self.ids.CI_StripTool.text, self.ids.CI_SFE.text, self.ids.CI_SFE_TOLMin.text,
        self.ids.CI_SFE_TOLPlus.text, self.ids.CI_STE.text, self.ids.CI_STE_TOLMin.text, self.ids.CI_STE_TOLPlus.text,
        self.ids.CI_CrI.active,self.ids.CI_ASM.active]

    def retrieve_cutting_data(self):
        self.ids.err_label.text= ''

        if self.ids.CI_CoreWireColor.text=='':
            for i in self.Cut_list_Core:
                if i[2]=='':
                    self.ids.CI_CoreWireColor.text=i[0]
                    self.clear_screen()
                    self.clear_color()
                    return
            self.ids.err_label.text='Core Wire is Empty.'
            return

        CC_check=[]
        for core_data in self.Cut_list_Core:
            CC_check.append(core_data[0])

        if self.ids.CI_CoreWireColor.text in CC_check:
            retrieve_index=CC_check.index(self.ids.CI_CoreWireColor.text)
            print(retrieve_index)

            if self.Cut_list_Core[retrieve_index][2]=='':
                self.clear_screen()
                self.clear_color()
                return
            else:
                self.ids.CI_StripTool.text=self.Cut_list_Core[retrieve_index][1]
                self.ids.CI_SFE.text=self.Cut_list_Core[retrieve_index][2]
                self.ids.CI_SFE_TOLMin.text=self.Cut_list_Core[retrieve_index][3]
                self.ids.CI_SFE_TOLPlus.text=self.Cut_list_Core[retrieve_index][4]
                self.ids.CI_STE.text=self.Cut_list_Core[retrieve_index][5]
                self.ids.CI_STE_TOLMin.text=self.Cut_list_Core[retrieve_index][6]
                self.ids.CI_STE_TOLPlus.text=self.Cut_list_Core[retrieve_index][7]
                self.ids.CI_CrI.active=self.Cut_list_Core[retrieve_index][8]
                self.ids.CI_ASM.active=self.Cut_list_Core[retrieve_index][9]
                self.clear_color()

        else:
            self.ids.err_label.text= 'Core is not available'

    def modify_cutting_data(self):
        self.ids.err_label.text= ''

        CC_check=[]
        for core_data in self.Cut_list_Core:
            CC_check.append(core_data[0])

        if self.ids.CI_CoreWireColor.text in CC_check:
            Cut_list_core=self.call_list_core()

            if not Cut_list_core == None:
                modify_index=CC_check.index(self.ids.CI_CoreWireColor.text)
                self.Cut_list_Core[modify_index]=Cut_list_core
                self.Show_Data_on_Screen()
                print(self.Cut_list_Com)

                try:
                    if self.Cut_list_Core[modify_index+1][2]=='':
                        self.ids.CI_CoreWireColor.text=self.Cut_list_Core[modify_index+1][0]
                        self.clear_screen()
                        self.ids.CI_StripTool.focus=True
                    else:
                        self.ids.CI_CoreWireColor.text=''
                        self.clear_screen()

                except IndexError:
                    self.ids.CI_CoreWireColor.text=''
                    self.clear_screen()

        elif self.ids.CI_CoreWireColor.text=='':
            self.ids.err_label.text= 'Core is empty'
            self.clear_screen()
        else:
            self.ids.err_label.text= 'Core is not available'
            self.clear_screen()


class FixedTextInput(TextInput):
    max_length = 39 # Is one lesser than required amount

    def insert_text(self, substring, from_undo=False):
        if len(self.text) <= self.max_length:
            return super().insert_text(substring, from_undo=from_undo)

class PositiveTextInput(FixedTextInput):
    def insert_text(self, substring, from_undo=False):

        if self.text=='-':
            self.text=''
        else:
            return super().insert_text(substring, from_undo=from_undo)

class App_design(App):
    Run_file = ObjectProperty(None)

    def build(self):
        self.Run_file = AddComponentPartNumber()
        return self.Run_file

App_design().run()

    # shirishkumar.lapp@gmail.com
    # tabrez.lapp@gmail.com
