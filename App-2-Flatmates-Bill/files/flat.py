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
