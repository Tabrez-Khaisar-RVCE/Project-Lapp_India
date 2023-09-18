
from functions import call_Crimp
from functions import crimpdetails
import os
from threading import Timer
import webbrowser
# from flask_classful import FlaskView
from flask import render_template
from flask import Flask
from datetime import date

def report_output(w,x,y,z):
    app = Flask(__name__)
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")

    newlist=y
    # ass_pname = ['a', 'b', 'c']
    # ass_list =[[["Connector housing Connector Assembly"],['wno1', 'pno1', 'tm1'],['wno2', 'pno2', 'tm2'], ['wno3', 'pno3', 'tm1']], [["Ink jet printing"],['wno4', 'pno4', 'tm4'],['wno5', 'pno5', 'tm5'], ['wno6', 'pno7', 'tm8']],[["Taping"],['wno9', 'pno9', 'tm9'],['wno10', 'pno10', 'tm10'], ['wno11', 'pno11', 'tm11']]]
    # for i in ass_list:
    #     ass = i[1][0][0]
    #     print(ass)
    loop1 = len(z) - 1
    loop12 = len(z[0])
    loop2 = loop12 - 1
    # a = call_Crimp()
    # b=crimpdetails()

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

    # for data in y:
    #     if not data[0] in crimp_component_number:
    #         crimp_component_number.append(data[0])
    #         crimp_repreat.append([data[0],1])
    #     else:
    #         crimp_repreat[crimp_component_number.index(data[0])][1]+=1
    # # print(crimp_component_number)
    # # print(crimp_repreat)
    #
    # for data in x:
    #     cut_component_number.append(data[0])
    #     cut_component_details.append([data[4],data[6],data[7]])
    # # print(cut_component_number)
    # # print(cut_component_details)
    # #
    # for component_number_in_crimp in crimp_component_number:
    #     if component_number_in_crimp in cut_component_number:
    #         y[crimp_component_number.index(component_number_in_crimp)]+=cut_component_details[cut_component_number.index(component_number_in_crimp)]
    #         for i in range(crimp_repreat[crimp_component_number.index(data[0])][1]):
    #             if i ==0:continue
    #             y[crimp_component_number.index(component_number_in_crimp)+i]+=cut_component_details[cut_component_number.index(component_number_in_crimp)]
    #
    # print(y)

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route('/cutting')
    def cutting_report():
        return render_template("cutting.html",w=w,x=x)


    @app.route('/crimping')
    def crimping_report():
        return render_template("crimping.html",w=w,y=y,x=x)

    @app.route('/inspection')
    def inspection_report():
        return render_template("inspection.html")

    @app.route('/assembly')
    def assembly_report():
        return render_template("assembly.html", z=z, loop1=loop1, loop2=loop2)

    # @app.route('/try')
    # def try_report():
    #     return render_template("try.html", ass_list=ass_list, loop1=loop1, loop2=loop2, ass_pname=ass_pname)

    def open_browser():
      webbrowser.open_new('http://127.0.0.1:2000/')

    Timer(1, open_browser).start()
    app.run(port=2000)
