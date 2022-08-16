import os
import webbrowser
from fpdf import FPDF

class Bill:
    def __init__(self, amount,period):
        self.amount=amount
        self.period=period

class Flatmate:
    def __init__(self,name,day_in_house):
        self.name=name
        self.day_in_house=day_in_house
    
    def pay(self,bill,flatmate):
        weight= self.day_in_house/(self.day_in_house+flatmate.day_in_house)
        to_pay=bill.amount*weight
        return to_pay

class pdfReport:

    def __init__(self,fileName) -> None:
        self.fileName=fileName
    
    def generate(self,flatmate1,flatmate2,bill):
        flatmate1_pay=str(round(flatmate1.pay(bill,flatmate2),2))
        flatmate2_pay=str(round(flatmate2.pay(bill,flatmate1),2))
        pdf=FPDF('P','pt','A4')
        pdf.add_page()
        pdf.image('/home/kourosh/Desktop/Learning/OOP-Python/App-2-Flatmates-Bill/files/house.png',w=30,h=30)

        pdf.set_font(family='Times',size=24, style='B')
        pdf.cell(0,80,txt='Flatmate Bill', border=0, align='C', ln=1)
        
        pdf.set_font(family='Times',size=14, style='B')
        pdf.cell(100,40,txt='Period:', border=0)
        pdf.cell(150,40,txt=bill.period, border=0, ln=1)

        pdf.set_font(family='Times',size=12, style='B')
        pdf.cell(100,25,txt=flatmate1.name, border=0)
        pdf.cell(100,25,txt=flatmate1_pay, border=0, ln=1)

        pdf.cell(100,25,txt=flatmate2.name, border=0)
        pdf.cell(100,25,txt=flatmate2_pay, border=0, ln=1)

        pdf.output(self.fileName)
        webbrowser.open('file://'+ os.path.realpath(self.fileName))




bill=Bill(120,'March 2021')
john=Flatmate('John',20)
marry=Flatmate('Marry',25)
# print(f'john has to pay {john.pay(bill,marry)}')
# print(f'marry has to pay {john.pay(bill,john)}')
report=pdfReport('Report1.pdf')
report.generate(john,marry,bill)

