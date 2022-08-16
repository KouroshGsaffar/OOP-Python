from flat import *
from report import *



amount=float(input('Hey user, Please enter the bill amount: '))
period=input('What is the bill period? e.g. December 2020: ')

first_flatmate=Flatmate(input('Please enter your name: '),float(input('Please enter the number of days you live in house : ')))
second_flatmate=Flatmate(input("Please enter your flatmate's name: "),float(input('Please enter the number of days you live in house : ')))
bill=Bill(amount,period)
# john=Flatmate('John',20)
# marry=Flatmate('Marry',25)
# print(f'john has to pay {john.pay(bill,marry)}')
# print(f'marry has to pay {john.pay(bill,john)}')
report=pdfReport(f'{period}.pdf')
report.generate(first_flatmate,second_flatmate,bill)

