from kivy.app import App
from kivy.lang import Builder
# from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from Push_Pop_screens import Push_Pop_screens
from kivy.properties import ObjectProperty
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.recycleview import RecycleView
from kivy.metrics import dp
import os

class Crimping_table_Input(BoxLayout):
    Cut_list_Com=[]
    Cut_list_Com_finalised=[]
    Remove_list=[]
    Component_Validation=[False,[['','pizza','black'],['','black','burger'],['','qwert','noodles']]] # component_availability_db(component_number)
    Headings=[]
     # [],{component_number:[True,[],[],[]],component_number:[[],[],[]]}
    Headings=[{'text': 'Core SL','size_hint_x':None,'width':dp(5)}, {'text':'Core Wire Color','bold':True}, {'text':'FE \n Marker Details and PNO','bold':True},
    {'text':'FE \n Crimp Type','bold':True}, {'text':'FE \n Terminal PNO','bold':True}, {'text':'FE \n Crimp Height','bold':True},
    {'text':'FE \n Pull Force','bold':True},{'text':'FE \n Crimp Instruction','bold':True},{'text':'FE \n Crimp Tool','bold':True},
    {'text':'TE \n Marker Details and PNO','bold':True},{'text':'TE \n Crimp Type','bold':True},{'text':'TE \n Terminal PNO','bold':True},
    {'text':'TE \n Crimp Height','bold':True},{'text':'TE \n Pull Force','bold':True},{'text':'TE \n Crimp Instruction','bold':True},
    {'text':'TE \n Crimp Tool','bold':True},{'text':'Assembly','bold':True}]

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        if self.Component_Validation[0]==True:
            for component_details in self.Component_Validation[1]:
                self.Cut_list_Com.append(component_details)

            self.ids.Add_cut_data.disabled=True
            self.ids.CI_CableDesc.disabled=True
            self.ids.CI_CoreWireColor.disabled=True

        print(self.Cut_list_Com)

        for i in self.Cut_list_Com:
            for j in i:
                self.Headings.append({'text':j,'bold':False})
            if len(i)==3:
                for j in range(20):
                    self.Headings.append({'text':'','bold':False})

        print(self.Cut_list_Com)
        self.ids.tablular_data.data = self.Headings
        print(self.Cut_list_Com)

    def Show_Data_on_Screen(self):
        self.Headings=[{'text': 'Cable SL','bold':True}, {'text':'Cable Description','bold':True}, {'text':'Core Wire color','bold':True},
        {'text':'QTY','bold':True}, {'text':'Cutting Machine/Tool','bold':True}, {'text':'Cable Cut Length in mm','bold':True},
        {'text':'TOL-','bold':True},{'text':'Tol+','bold':True},{'text':'Jacket Remove Machine/Tool','bold':True},
        {'text':'Jacket FE cut length','bold':True},{'text':'TOL-','bold':True},{'text':'TOL+','bold':True},
        {'text':'Jacket TE cut length','bold':True},{'text':'TOL-','bold':True},{'text':'TOL+','bold':True},
        {'text':'Stripping tool','bold':True},{'text':'Strip FE length','bold':True},{'text':'TOL-','bold':True},{'text':'TOL+','bold':True},
        {'text':'Strip TE length','bold':True},{'text':'TOL-','bold':True},{'text':'TOL+','bold':True},{'text':'Crimp','bold':True}]

        for i in self.Cut_list_Com:
            for j in i:
                if type(j)==bool:
                    self.Headings.append({'text':str(j),'bold':False})
                    break
                self.Headings.append({'text':j,'bold':False})

            if len(i)==3:
                for j in range(20):
                    self.Headings.append({'text':'','bold':False})

        self.ids.tablular_data.data = self.Headings

    def list_converter(self,data_list):

        Cut_length=str(float(data_list[5])-float(data_list[6])) + ' to ' + str(float(data_list[5])+float(data_list[7]))
        Jacket_FE=str(float(data_list[9])-float(data_list[10])) + ' to ' + str(float(data_list[9])+float(data_list[11]))
        Jacket_TE=str(float(data_list[12])-float(data_list[13])) + ' to ' + str(float(data_list[12])+float(data_list[14]))
        Strip_FE=str(float(data_list[16])-float(data_list[17])) + ' to ' + str(float(data_list[16])+float(data_list[18]))
        Strip_TE=str(float(data_list[19])-float(data_list[20])) + ' to ' + str(float(data_list[19])+float(data_list[21]))

        self.Cut_list_Com_finalised=[data_list[0],data_list[1],data_list[2],data_list[3],
        data_list[4], Cut_length, data_list[8], Jacket_FE, Jacket_TE, data_list[15] , Strip_FE, Strip_TE,data_list[22]]

    def clear_screen(self):
        self.ids.CI_CableDesc.text=''
        self.ids.CI_CoreWireColor.text=''
        self.ids.CI_QTY.text=''
        self.ids.CI_CutTool.text=''
        self.ids.CI_Cut.text=''
        self.ids.CI_Cut_TOLMin.text=''
        self.ids.CI_Cut_TOLPlus.text=''
        self.ids.CI_JacketTool.text=''
        self.ids.CI_JFE.text=''
        self.ids.CI_JFE_TOLMin.text=''
        self.ids.CI_JFE_TOLPlus.text=''
        self.ids.CI_JTE.text=''
        self.ids.CI_JTE_TOLMin.text=''
        self.ids.CI_JTE_TOLPlus.text=''
        self.ids.CI_StripTool.text=''
        self.ids.CI_SFE.text=''
        self.ids.CI_SFE_TOLMin.text=''
        self.ids.CI_SFE_TOLPlus.text=''
        self.ids.CI_STE.text=''
        self.ids.CI_STE_TOLMin.text=''
        self.ids.CI_STE_TOLPlus.text=''
        self.ids.CI_CrI.active=False
        self.ids.CI_Cable_SL.focus=True

        self.ids.CI_Cable_SL.background_color=(1,1,1,1)
        self.ids.CI_CableDesc.background_color=(1,1,1,1)
        self.ids.CI_QTY.background_color=(1,1,1,1)
        self.ids.CI_QTY.background_color=(1,1,1,1)
        self.ids.CI_Cut.background_color=(1,1,1,1)
        self.ids.CI_JFE.background_color=(1,1,1,1)
        self.ids.CI_JTE.background_color=(1,1,1,1)
        self.ids.CI_SFE.background_color=(1,1,1,1)
        self.ids.CI_STE.background_color=(1,1,1,1)
        self.ids.CI_CutTool.background_color=(1,1,1,1)
        self.ids.CI_JacketTool.background_color=(1,1,1,1)
        self.ids.CI_StripTool.background_color=(1,1,1,1)


    def call_list(self):

        self.ids.err_label.text=''

        err_detail=False

        if self.ids.CI_Cable_SL.text == '':
            err_detail=True
            self.ids.err_label.text= 'Cable SL,'
            self.ids.CI_Cable_SL.background_color=(1,0,0,0.8)
        else:
            self.ids.CI_Cable_SL.background_color=(1,1,1,1)

        if self.ids.CI_CableDesc.text == '':
            err_detail=True
            self.ids.err_label.text+= 'Cable Description,'
            self.ids.CI_CableDesc.background_color=(1,0,0,0.8)
        else:
            self.ids.CI_CableDesc.background_color=(1,1,1,1)

        if self.ids.CI_CoreWireColor.text == '' or self.ids.CI_CoreWireColor.text == '-':
            self.ids.CI_JacketTool.text='NA'
            self.ids.CI_CoreWireColor.text= '-'
            self.ids.CI_JFE.text='0'
            self.ids.CI_JFE_TOLMin.text='0'
            self.ids.CI_JFE_TOLPlus.text='0'
            self.ids.CI_JTE.text='0'
            self.ids.CI_JTE_TOLMin.text='0'
            self.ids.CI_JTE_TOLPlus.text='0'

        if self.ids.CI_QTY.text == '' or self.ids.CI_QTY.text =='0' or self.ids.CI_QTY.text =='-':
            err_detail=True
            self.ids.err_label.text+= 'Cable QTY,'
            self.ids.CI_QTY.background_color=(1,0,0,0.8)
        else:
            self.ids.CI_QTY.background_color=(1,1,1,1)

        if err_detail==True:
            self.ids.err_label.text+= ' is empty.'
            return None

        if self.ids.CI_Cut.text=='' or self.ids.CI_Cut.text=='-': self.ids.CI_Cut.text='0'
        if self.ids.CI_Cut_TOLMin.text==''or self.ids.CI_Cut_TOLMin.text=='-': self.ids.CI_Cut_TOLMin.text='0'
        if self.ids.CI_Cut_TOLPlus.text==''or self.ids.CI_Cut_TOLPlus.text=='-':self.ids.CI_Cut_TOLPlus.text='0'
        if self.ids.CI_JFE.text==''or self.ids.CI_JFE.text=='-':self.ids.CI_JFE.text='0'
        if self.ids.CI_JFE_TOLMin.text==''or self.ids.CI_JFE_TOLMin.text=='-':self.ids.CI_JFE_TOLMin.text='0'
        if self.ids.CI_JFE_TOLPlus.text==''or self.ids.CI_JFE_TOLPlus.text=='-':self.ids.CI_JFE_TOLPlus.text='0'
        if self.ids.CI_JTE.text==''or self.ids.CI_JTE.text=='-':self.ids.CI_JTE.text='0'
        if self.ids.CI_JTE_TOLMin.text==''or self.ids.CI_JTE_TOLMin.text=='-':self.ids.CI_JTE_TOLMin.text='0'
        if self.ids.CI_JTE_TOLPlus.text==''or self.ids.CI_JTE_TOLPlus.text=='-':self.ids.CI_JTE_TOLPlus.text='0'
        if self.ids.CI_SFE.text==''or self.ids.CI_SFE.text=='-':self.ids.CI_SFE.text='0'
        if self.ids.CI_SFE_TOLMin.text==''or self.ids.CI_SFE_TOLMin.text=='-':self.ids.CI_SFE_TOLMin.text='0'
        if self.ids.CI_SFE_TOLPlus.text==''or self.ids.CI_SFE_TOLPlus.text=='-':self.ids.CI_SFE_TOLPlus.text='0'
        if self.ids.CI_STE.text==''or self.ids.CI_STE.text=='-':self.ids.CI_STE.text='0'
        if self.ids.CI_STE_TOLMin.text==''or self.ids.CI_STE_TOLMin.text=='-':self.ids.CI_STE_TOLMin.text='0'
        if self.ids.CI_STE_TOLPlus.text==''or self.ids.CI_STE_TOLPlus.text=='-':self.ids.CI_STE_TOLPlus.text='0'

        err_calc=False

        Cut_length_TolMin=float(self.ids.CI_Cut.text)-float(self.ids.CI_Cut_TOLMin.text)
        Jacket_FE_TolMin=float(self.ids.CI_JFE.text)-float(self.ids.CI_JFE_TOLMin.text)
        Jacket_TE_TolMin=float(self.ids.CI_JTE.text)-float(self.ids.CI_JTE_TOLMin.text)
        Strip_FE_TolMin=float(self.ids.CI_SFE.text)-float(self.ids.CI_SFE_TOLMin.text)
        Strip_TE_TolMin=float(self.ids.CI_STE.text)-float(self.ids.CI_STE_TOLMin.text)

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
        if not self.ids.CI_StripTool.text in ['3','4']:
            err_tool=True
            self.ids.CI_StripTool.background_color=(1,0,0,0.8)
            self.ids.err_label.text+= 'Strip Tool, '
        else:
            self.ids.CI_StripTool.background_color=(1,1,1,1)
            # StripToolDetails_db(plant_id)
        if err_tool==True:
            self.ids.err_label.text+= 'not available in the Database.'
            return None


        return [self.ids.CI_Cable_SL.text,self.ids.CI_CableDesc.text,self.ids.CI_CoreWireColor.text,self.ids.CI_QTY.text,
        self.ids.CI_CutTool.text, self.ids.CI_Cut.text, self.ids.CI_Cut_TOLMin.text,self.ids.CI_Cut_TOLPlus.text,self.ids.CI_JacketTool.text,
        self.ids.CI_JFE.text,self.ids.CI_JFE_TOLMin.text,self.ids.CI_JFE_TOLPlus.text, self.ids.CI_JTE.text, self.ids.CI_JTE_TOLMin.text,
        self.ids.CI_JTE_TOLPlus.text, self.ids.CI_StripTool.text, self.ids.CI_SFE.text, self.ids.CI_SFE_TOLMin.text, self.ids.CI_SFE_TOLPlus.text,
        self.ids.CI_STE.text, self.ids.CI_STE_TOLMin.text, self.ids.CI_STE_TOLPlus.text,self.ids.CI_CrI.active]

    def cutting_data(self): # Fix
        SL_check=[]
        for individual_cut_details in self.Cut_list_Com:
            SL_check.append(individual_cut_details[0])
            print(SL_check)

        if self.Component_Validation[0]==True:
            for Removed_list in self.Remove_list:
                renewed_row=['']
                renewed_row+=(Removed_list[1:3])
                self.Cut_list_Com.append(renewed_row)
                self.Show_Data_on_Screen()
                self.ids.Add_cut_data.disabled=True
            self.Remove_list=[]
            return

        if self.ids.CI_Cable_SL.text in SL_check: self.ids.err_label.text= 'Cable SL is repeated.'
        else:
            Cut_list_SL=self.call_list()
            if not Cut_list_SL == None:
                print(Cut_list_SL)
                self.Cut_list_Com.append(Cut_list_SL)
                self.Show_Data_on_Screen()

                try:
                    self.ids.CI_Cable_SL.text=str(int(self.ids.CI_Cable_SL.text)+1)
                except ValueError:
                    self.ids.CI_Cable_SL.text=''
                self.clear_screen()

    def remove_cutting_data(self):
        SL_check=[]
        self.ids.err_label.text= ''

        for individual_cut_details in self.Cut_list_Com:
            SL_check.append(individual_cut_details[0])

        if self.ids.CI_Cable_SL.text in SL_check and self.Component_Validation[0]==True:
            remove_index=SL_check.index(self.ids.CI_Cable_SL.text)
            self.Remove_list.append(self.Cut_list_Com[remove_index])
            del self.Cut_list_Com[remove_index]
            self.Show_Data_on_Screen()
            self.clear_screen()
            self.ids.Add_cut_data.disabled=False
            return

        if self.ids.CI_Cable_SL.text in SL_check:
            remove_index=SL_check.index(self.ids.CI_Cable_SL.text)
            del self.Cut_list_Com[remove_index]
            self.Show_Data_on_Screen()
            self.clear_screen()
        else:
            self.ids.err_label.text= 'SL is not available'
            print(self.Cut_list_Com)

    def retrieve_cutting_data(self):
        self.ids.err_label.text= ''

        if self.Component_Validation[0]==True and self.ids.CI_Cable_SL.text=='':

            for retrieve_data in self.Cut_list_Com:
                if len(retrieve_data)==3:
                    self.clear_screen()
                    self.ids.CI_CableDesc.text=retrieve_data[1]
                    self.ids.CI_CoreWireColor.text=retrieve_data[2]
                    return

        SL_check=[]
        for individual_cut_details in self.Cut_list_Com:
            SL_check.append(individual_cut_details[0])

        if self.ids.CI_Cable_SL.text in SL_check:
            retrieve_data=[]
            retrieve_index=SL_check.index(self.ids.CI_Cable_SL.text)
            retrieve_data=self.Cut_list_Com[retrieve_index]
            self.ids.CI_CableDesc.text=retrieve_data[1]
            self.ids.CI_CoreWireColor.text=retrieve_data[2]
            self.ids.CI_QTY.text=retrieve_data[3]
            self.ids.CI_CutTool.text=retrieve_data[4]
            self.ids.CI_Cut.text=retrieve_data[5]
            self.ids.CI_Cut_TOLMin.text=retrieve_data[6]
            self.ids.CI_Cut_TOLPlus.text=retrieve_data[7]
            self.ids.CI_JacketTool.text=retrieve_data[8]
            self.ids.CI_JFE.text=retrieve_data[9]
            self.ids.CI_JFE_TOLMin.text=retrieve_data[10]
            self.ids.CI_JFE_TOLPlus.text=retrieve_data[11]
            self.ids.CI_JTE.text=retrieve_data[12]
            self.ids.CI_JTE_TOLMin.text=retrieve_data[13]
            self.ids.CI_JTE_TOLPlus.text=retrieve_data[14]
            self.ids.CI_StripTool.text=retrieve_data[15]
            self.ids.CI_SFE.text=retrieve_data[16]
            self.ids.CI_SFE_TOLMin.text=retrieve_data[17]
            self.ids.CI_SFE_TOLPlus.text=retrieve_data[18]
            self.ids.CI_STE.text=retrieve_data[19]
            self.ids.CI_STE_TOLMin.text=retrieve_data[20]
            self.ids.CI_STE_TOLPlus.text=retrieve_data[21]
            self.ids.CI_CrI.active=retrieve_data[22]
            # self.ids.CI_CrI.active=False
            self.ids.CI_Cable_SL.focus=True
        else:
            self.ids.err_label.text= 'SL is not available'

    def modify_cutting_data(self):
        SL_check=[]
        Details_check=[]
        New_Details_check=[]
        self.ids.err_label.text= ''
        modify_index=int()

        for individual_cut_details in self.Cut_list_Com:
            SL_check.append(individual_cut_details[0])

        for individual_cut_details in self.Cut_list_Com:
            if len(individual_cut_details)==3:
                New_Details_check=individual_cut_details[1:]
                break

        if self.Component_Validation[0]==True:
            for individual_cut_details in self.Cut_list_Com:
                if len(individual_cut_details)>3:
                    Details_check.append(individual_cut_details[0:3])
            if not [self.ids.CI_Cable_SL.text,self.ids.CI_CableDesc.text,self.ids.CI_CoreWireColor.text] in Details_check:
                if [self.ids.CI_CableDesc.text,self.ids.CI_CoreWireColor.text] == New_Details_check and [self.ids.CI_CableDesc.text,self.ids.CI_CoreWireColor.text] != ['','']:
                    for retrieve_data in self.Cut_list_Com:
                        if len(retrieve_data)==3:
                            Cut_list_SL=self.call_list()
                            if not Cut_list_SL == None and not self.ids.CI_Cable_SL.text in SL_check:
                                modify_index=self.Cut_list_Com.index(retrieve_data)
                                self.Cut_list_Com[modify_index]=Cut_list_SL
                                self.Show_Data_on_Screen() # change
                                try:
                                    self.clear_screen()
                                    self.ids.CI_Cable_SL.text=''
                                    self.retrieve_cutting_data()
                                    break
                                except IndexError:
                                    self.ids.CI_Cable_SL.text=''
                                    self.clear_screen()
                                    break

                            elif self.ids.CI_Cable_SL.text in SL_check:
                                self.ids.err_label.text+= ' SL is already available.'
                    print(self.Cut_list_Com)
                    return
                else:
                    self.ids.err_label.text+= ' Cannot Modify.'
                    return


        if self.ids.CI_Cable_SL.text in SL_check and self.ids.CI_Cable_SL.text!='':
            Cut_list_SL=self.call_list()
            if not Cut_list_SL == None:
                modify_index=SL_check.index(self.ids.CI_Cable_SL.text)
                self.Cut_list_Com[modify_index]=Cut_list_SL
                self.Show_Data_on_Screen() # change
                print(self.Cut_list_Com)

                try:
                    self.ids.CI_Cable_SL.text=SL_check[modify_index+1]
                    self.retrieve_cutting_data()
                except IndexError:
                    self.ids.CI_Cable_SL.text=''
                    self.clear_screen()

        elif self.ids.CI_Cable_SL.text=='':
            self.ids.err_label.text= 'SL is empty'
        else:
            self.ids.err_label.text= 'SL is not available'

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

class check(App):
    Run_file = ObjectProperty(None)

    def build(self):
        self.icon = 'Design_considerations/Images/App_Icon.png'
        self.Run_file = Crimping_table_Input()
        return self.Run_file

check().run()
