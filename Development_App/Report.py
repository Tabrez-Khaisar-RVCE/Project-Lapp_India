from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.uix.textinput import TextInput
from BACKEND_DB import WO_details_db
from BACKEND_PY import WO_Excel_Input_py
from BACKEND_DB import Validate_Terminal_PNO_db
from BACKEND_DB import Enter_CD_db
from BACKEND_DB import Delete_Component_details
from BACKEND_DB import Retrieve_terminal_db
from BACKEND_DB import Modify_terminal_db
from BACKEND_DB import Delete_terminal_db
from BACKEND_DB import Add_Terminal_db
from BACKEND_DB import Component_Details_db
from BACKEND_DB import WO_details_completed_db
from BACKEND_DB import updatingqty
from BACKEND_DB import Modify_WO_recheck_db

Builder.load_file('Report.kv')

class REP_MOD_Terminal(GridLayout):

    def Details(self):
        if self.ids.Terminal_PNO.text=='':
            self.ids.err_label.text='Terminal_PNO is empty'
            return

        if self.ids.Terminal_Strip_Length.text=='-' or self.ids.Terminal_Strip_Length.text=='':
            self.ids.Terminal_Strip_Length.text='0'
        if self.ids.Terminal_TOLMin.text=='-' or self.ids.Terminal_TOLMin.text=='':
            self.ids.Terminal_TOLMin.text='0'
        if self.ids.Terminal_TOLPlus.text=='-' or self.ids.Terminal_TOLPlus.text=='':
            self.ids.Terminal_TOLPlus.text='0'

        if float(self.ids.Terminal_Strip_Length.text)-float(self.ids.Terminal_TOLMin.text)<=0:
            self.ids.err_label.text='Strip length cannot be -ve or 0.'
            return
        return [self.ids.Terminal_PNO.text,self.ids.Terminal_Strip_Length.text,self.ids.Terminal_TOLMin.text,self.ids.Terminal_TOLPlus.text]

    def clear_screen(self):
        self.ids.Terminal_PNO.text=''
        self.ids.Terminal_Strip_Length.text=''
        self.ids.Terminal_TOLMin.text=''
        self.ids.Terminal_TOLPlus.text=''
        self.ids.Terminal_PNO.focus=True

    def Add_details(self):
        if Validate_Terminal_PNO_db(self.ids.Terminal_PNO.text)==True:
            self.ids.err_label.text='Terminal Part is already Available.'
            return

        self.ids.err_label.text=''
        Terminal_Part_data=self.Details()
        if not Terminal_Part_data==None:
            Add_Terminal_db(Terminal_Part_data)
            self.clear_screen()

    def Retrieve_details(self):
        Terminal_Part_data= Retrieve_terminal_db(self.ids.Terminal_PNO.text)

        if Terminal_Part_data==None:
            self.ids.err_label.text='Terminal Part Not Available.'
            return
        else:
            self.ids.err_label.text=''
            self.ids.Terminal_Strip_Length.text=str(Terminal_Part_data[0])
            self.ids.Terminal_TOLMin.text=str(Terminal_Part_data[1])
            self.ids.Terminal_TOLPlus.text=str(Terminal_Part_data[2])

    def Modify_details(self):
        if Validate_Terminal_PNO_db(self.ids.Terminal_PNO.text)==False:
            self.ids.err_label.text='Terminal Part Not Available.'
            return

        self.ids.err_label.text=''
        Terminal_Part_data=self.Details()
        if not Terminal_Part_data==None:
            Modify_terminal_db(Terminal_Part_data)
            self.clear_screen()

    def Remove_details(self):
        if Validate_Terminal_PNO_db(self.ids.Terminal_PNO.text)==False:
            self.ids.err_label.text='Terminal Part Not Available.'
            return

        Delete_terminal_db(self.ids.Terminal_PNO.text)
        self.clear_screen()

class REP_EXP_Report(BoxLayout):
    validation=[]
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def get_WO_details(self):
        WO_number=self.ids.Word_Order_Number.text
        self.validation=WO_details_db(WO_number)
        print(self.validation)
        if self.validation[0]==False:
            self.ids.Error_label.text='Work order not available.'
        elif self.validation[2]-self.validation[1]==0:
            self.ids.Error_label.text='Work order QTY is 0.'
        else:
            self.ids.Word_Order_Number.disabled=True
            self.ids.FG_Part_Num.text=self.validation[0]
            self.ids.WO_QTY.text=str(self.validation[2]-self.validation[1])
            self.ids.JT_QTY.disabled=False
            self.ids.Confirm_button.text='Download'
            self.ids.JT_QTY.focus=True
            self.ids.Error_label.text=''


    def QTY_match(self):
        if self.ids.JT_QTY.text=='' or self.ids.JT_QTY.text=='0'or self.ids.JT_QTY.text=='-':self.ids.Error_label.text='JT is 0.'
        elif int(self.ids.JT_QTY.text)>self.validation[2]-self.validation[1]:
            self.ids.Error_label.text='JT is exceeding WO QTY available.'
        elif int(self.ids.JT_QTY.text)<=self.validation[2]-self.validation[1]:
            # Download_report_db(self.validation[0],self.ids.JT_QTY.text,self.validation[1]) # should print report and update database
            # Check if 2 people ordered wo at the same time
            self.ids.Error_label.text='Report Made, for PNO: ' + self.validation[0]
            self.ids.Confirm_button.text='Submit'
            self.ids.WO_QTY.text=''
            self.ids.FG_Part_Num.text=''
            self.ids.Word_Order_Number.disabled=False
            self.ids.JT_QTY.text=''
            self.ids.JT_QTY.disabled=True
            self.ids.Word_Order_Number.focus=True
            self.ids.Word_Order_Number.text=''

class Retrieve_xlsx_file(BoxLayout):
    confirm = ObjectProperty(None)
    cancel = ObjectProperty(None)
    file_location = ObjectProperty(None)

class REP_IMP_WorkOrder(BoxLayout):
    file_accepted_path=[]

    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_Retrieve_xlsx_file(self):
        content = Retrieve_xlsx_file(confirm=self.take_file_location,cancel=self.dismiss_popup)
        self._popup = Popup(title="WO File location", content=content, size_hint=(0.9, 0.9))
        self._popup.open()

    def take_file_location(self, file_path,file_text):
        if file_path=='':
            self.ids.file_location_main.text='Choose WO Location'
        else:
            self.ids.file_location_main.text=file_text
            self.file_accepted_path=file_path
        self.dismiss_popup()

    def confirm_file(self):
        print(self.file_accepted_path)
        verification = WO_Excel_Input_py(self.file_accepted_path)
        print(self.file_accepted_path)
        if verification[0]==False:
            self.ids.Error_label.text=verification[1]
        elif verification[0]==True:
            self.ids.Error_label.text='WO Sheet Accepted.'

class REP_MOD_Component(BoxLayout):

    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def on_screen_display(self,Component,Description,corecolor):
        data_holder=[]
        for cores in corecolor:
            data_holder.append({'text':cores})

        self.ids.Display_component_Number.text=Component
        self.ids.Display_component_Description.text=Description
        self.ids.tablular_data_cores.data=data_holder

    def Add_details(self):
        if self.ids.Component_Number.text=='':
            self.ids.err_label.text='Component Number is Empty.'
            return

        self.ids.err_label.text=''
        Availability = Component_Details_db(self.ids.Component_Number.text)

        if self.ids.Description.text=='':
            self.ids.err_label.text='Component Description is Empty.'
            return
        if self.ids.Core.text=='':
            self.ids.err_label.text='Component Core is Empty.'
            return

        if Availability[0]==False:
            Enter_CD_db([self.ids.Component_Number.text,self.ids.Core.text,self.ids.Description.text])
            self.on_screen_display(self.ids.Component_Number.text,self.ids.Description.text,[self.ids.Core.text])
        else:
            if self.ids.Core.text in Availability[2]:
                self.ids.err_label.text='Component Core is Repeated.'
                return
            Enter_CD_db([self.ids.Component_Number.text,self.ids.Core.text,self.ids.Description.text])
            self.on_screen_display(self.ids.Component_Number.text,Availability[1],Availability[2]+[self.ids.Core.text])

        self.ids.Core.text=''
        self.ids.Core.focus=True

    def Remove_details(self):
        Availability = Component_Details_db(self.ids.Component_Number.text)
        if Availability[0]==True:
            self.ids.err_label.text=''
            if self.ids.Core.text=='' :
                Delete_Component_details(self.ids.Component_Number.text,'')
                self.on_screen_display('','',[])
            else:
                if self.ids.Core.text in Availability[2]:
                    Delete_Component_details(self.ids.Component_Number.text,self.ids.Core.text)
                    if len(Availability[2])==1:self.on_screen_display('','',[])
                    else:
                        print(Availability[2])
                        a=Availability[2]
                        a.remove(self.ids.Core.text)
                        self.on_screen_display(self.ids.Component_Number.text,Availability[1],a)
                else:
                    self.ids.err_label.text='Core not available.'

        else: self.ids.err_label.text='Not available in the Database.'

    def Retrieve_details(self):
        Availability = Component_Details_db(self.ids.Component_Number.text)

        if Availability[0]==True:
            self.ids.err_label.text=''
            self.on_screen_display(self.ids.Component_Number.text,Availability[1],Availability[2])
            self.ids.Description.text=Availability[1]
            self.ids.Core.text=''
            self.ids.Core.focus=True

        else: self.ids.err_label.text='Not available in the Database.'

class REP_MOD_WorkOrder_modify(GridLayout):

    def Retrieve_details(self):
        WO_details=WO_details_db(self.ids.Work_Order.text)
        if WO_details==[False]:
            WO_details_recheck=WO_details_completed_db(self.ids.Work_Order.text)
            if WO_details_recheck==False:
                self.ids.err_label.text='Work Order Not available.'
            else:
                self.ids.err_label.text=''
                self.ids.Total_QTY.text=str(WO_details_recheck[0])
                self.ids.Delivered_QTY.text=str(WO_details_recheck[0])
        else:
            self.ids.err_label.text=''
            self.ids.Total_QTY.text=str(WO_details[2])
            self.ids.Delivered_QTY.text=str(WO_details[1])

    def Modify_details(self):
        WO_details=WO_details_db(self.ids.Work_Order.text)
        if self.ids.Delivered_QTY.text=='-' or self.ids.Delivered_QTY.text=='':self.ids.Delivered_QTY.text='0'
        if WO_details==[False]:
            WO_details_recheck=WO_details_completed_db(self.ids.Work_Order.text)
            if WO_details_recheck==False:
                self.ids.err_label.text='Work Order Not available.'
                return
            else:
                Modify_WO_recheck_db(self.ids.Work_Order.text,self.ids.Delivered_QTY.text)
        else:
            updatingqty(self.ids.Delivered_QTY.text,self.ids.Work_Order.text)

        self.ids.Work_Order.text=''
        self.ids.Total_QTY.text=''
        self.ids.Delivered_QTY.text=''

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

# [part_number,used_qty] #May need plant id #or err someone reduced qty.
