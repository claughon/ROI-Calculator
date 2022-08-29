from binascii import Incomplete
from ctypes import addressof


import locale
from socketserver import ThreadingUnixStreamServer
print(locale.setlocale(locale.LC_ALL, ''))

def m(x):
    return locale.currency(x, grouping=True)


def int_(x):
    x = x.replace("$", "").replace(" ", "").replace(",", "")
    for n in x:
        if n not in "0123456789.":
            print("ERROR: Enter a valid number")
            return False
        else: 
            return int(x)




class Return:

    def __init__(self):
        self.properties = {}
        self.income = {}
        self.monthly_expenses = {}
        self.cash_flow = []
        self.cash_on_cash_roi = {}

    def new_property(self):
        address = input("What is the address for this new property? ")
        if address not in self.properties:
            self.properties['address'] = address
        else:
            print("There is already a property her under that address.")


    def show(self):
        for address in self.properties.items():
            print("You have the following property ROI calculations stored with us: ")
            print(f"Address: {address}")
            edit = input("Would you like to edit any of your current property calculations? yes/no ")
            if 'y' or 'yes':
                print(self.properties.items())
            else: 
                self.properties.items() == {}
                print("You currently do not have any ROI calculations stored with us.")
                continue

    def monthly_income(self):
        rent = input(f"How much are you collecting in rent? ")
        self.income['rent'] = int_(rent)
        print("You are receiving " + m(int_(rent)) + " per month from rent.")
        laundry = input(f"How much are you collecting in laundry income? ")
        self.income['laundry'] = int_(laundry)
        print("You are receiving " + m(int_(laundry)) + " per month from laundry services.")
        storage = input(f"How much are you collecting in storage income? ")
        self.income['storage'] = int_(storage)
        print("You are reveiving " + m(int_(storage)) + " per month from storage services.")
        misc = input(f"How much are you collecting in any other forms of income from this property? ")
        self.income['misc'] = int_(misc)
        print("You are receiving " + m(int_(misc)) + " per month from miscellanious services provided.")
        rough_income = self.income.values()
        total_income = sum(rough_income)
        self.income['total_monthly_income'] = int(total_income)
        print("Your total montly income is " + m(total_income) + ".")

    def monthly_expenditures(self):
        taxes = input(f"How much do you pay in taxes per month? ")
        self.monthly_expenses['taxes'] = int_(taxes)
        print("You pay " + m(int_(taxes)) + " in taxes each month.")
        insurance = input(f"How much do you pay in insurance each month? ")
        self.monthly_expenses['insurance'] = int_(insurance)
        print("You pay " + m(int_(insurance)) + " for insurance each month.")
        utilities = input(f"How much do you pay in utilities each month? ")
        self.monthly_expenses['utilities'] = int_(utilities)
        print("You pay " + m(int_(utilities)) + " for utilities each month.")
        home_owners = input(f"How much do you pay in HOA fees per month? ")
        self.monthly_expenses['home_owners'] = int_(home_owners)
        print("You pay " + home_owners + " in HOA fees per month.")
        lawn_care = input(f"How much do you pay in lawn care and/or snow removal per month? ")
        self.monthly_expenses['lawn_care'] = int_(lawn_care)
        print("You pay " + m(int_(lawn_care)) + " in lawn care services per month.")
        vacancy = input(f"How much do you put aside towards vacancy each month? ")
        self.monthly_expenses['vacancy'] = int_(vacancy)
        print("You put aside " + m(int(vacancy)) + " for future vacancies, per month.")
        repairs = input(f"How much do you put aside for repairs each month? ")
        self.monthly_expenses['repairs'] = int_(repairs)
        print("You put aside " + m(int_(repairs)) + " for future repair costs per month.")
        capex = input(f"How much do you put aside for capital expenditures each month? ")
        self.monthly_expenses['capex'] = int_(capex)
        print("You put aside " + m(int_(capex)) + " for future expeditures, each month.")
        property_mgmt = input("How much do you pay for property management each month? ")
        self.monthly_expenses['property_mgmt'] = int_(property_mgmt)
        print("You pay " + m(int_(property_mgmt)) + " per month for property management services.")
        mortgage = input(f"How much do you pay for your mortgage each month? ")
        self.monthly_expenses['mortgage'] = int_(mortgage)
        print("You pay " + m(int_(mortgage)) + " per month for your mortgage.")
        rough_expenditures = self.monthly_expenses.values()
        total_expenditures = sum(rough_expenditures)
        self.monthly_expenses['total_expenditures'] = int(total_expenditures)
        print("Your total monthly expenditures were " + m(total_expenditures) + ".")

    def cash_in_pocket(self):
        cash_flowing = self.income['total_monthly_income'] - self.monthly_expenses['total_expenditures']
        self.cash_flow.append(cash_flowing)
        print("Your cash flow from the month is " + m(cash_flowing) + ".")
    

    def cash_roi(self): 
        down = input(f"How much did you put down for this property? ")
        self.cash_on_cash_roi['down'] = int_(down)
        print("You put " + m(int_(down)) + ".")
        closing = input(f"How much were the closing costs on this property? ")
        self.cash_on_cash_roi['closing'] = int_(closing)
        print("You spent " + m(int_(closing)) + " in closing costs.")
        rehab = input(f"How much did you spend for the rehab of this property? ")
        self.cash_on_cash_roi['rehab'] = int_(rehab)
        print("You spent " + m(int_(rehab)) + " on reahbilitation of the property.")
        other = input(f"Please, input any other monitary expenses that you had for this property. ")
        self.cash_on_cash_roi['other'] = int_(other)
        print("You spent " + m(int_(other)) + " on other expenses for this property.")
        investments = self.cash_on_cash_roi.values()
        total_investment = sum(investments)
        self.cash_on_cash_roi['total_investments'] = int(total_investment)
        print("You have a total investment of " + m(total_investment) + ", on this property.")

    def calculations(self):
        annual_cash_flow = self.cash_flow[0] * 12
        print("Your annual cash flow on this property is " + m(annual_cash_flow) + ".")      
        rate_of_investment = annual_cash_flow / self.cash_on_cash_roi['total_investments'] * 100
        print(f"Your overall rate of investment, on this property is {rate_of_investment}.")
       


class Main:

    def showInstructions():
        print("""Welcome to Your ROI Calculator:
        To begin select from the following list:
        [1] Add New Property
        [2] Edit Current Property
        [3] Quit""")

    def run():
        Main.showInstructions()
        my_returns = Return()
        
        while True:
            answer = input("How would you like to begin? ")
            answer = answer.strip()
            if answer == "1":
                my_returns.new_property()
                my_returns.monthly_income()
                my_returns.monthly_expenditures()
                my_returns.cash_in_pocket()
                my_returns.cash_roi()
                my_returns.calculations()
                continue
            if answer == "2":
                if my_returns.properties == {}:
                    print("You do not have any exisitng ROI calculations stored with us.")
                else:
                    my_returns.show()
            if answer == '3':
                break
            else:
                print("Input not recognized, please try again.")
                my_returns
Main.run()
myreturnsProgram = Main()