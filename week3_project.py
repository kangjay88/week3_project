from ast import Pass, Return
from binascii import Incomplete
from xml.etree.ElementTree import TreeBuilder

from traitlets import Integer


class Roi():
    def __init__(self, income):
        self.income= income
        self.finance = {}

    def squareone(self):
        while True:
            rentincome = input("Please type in your estimated monthly income for RENT. ")
            if rentincome.isnumeric():
                self.finance['RentIncome'] = rentincome
                break
            else:
                print("Error. Please type in a number with no punctuation or variables.Please round to the nearest dollar. ")
        while True:
            additionalincome = input("Do you have any other forms of monthly income (Ex: Laundry, Storage, etc.)? If so, please state the estimated number here: ")
            if additionalincome.isnumeric():
                self.finance['AddIncome'] = additionalincome
                break  
            else:
                print("Error. Please type in a number with no punctuation or variables.Please round to the nearest dollar. ")
        self.finance['TotalIncome'] = int(rentincome) + int(additionalincome)
        print(f"Your total income is {self.finance['TotalIncome']}")

    def squaretwo(self):
        while True:
            mortgage = input("What is your monthly mortgage rate?")
            if mortgage.isnumeric():
                self.finance['Mortage'] = mortgage
                break
            else:
                print("Error. Please type in a number with no punctuation or variables.Please round to the nearest dollar. ")
        while True:
            expenses = input("Please type in your TOTAL estimate monthly expense for Taxes, Insurance, Utilities, and HOA: ")
            if expenses.isnumeric():
                self.finance['MainExpenses'] = expenses
                break
            else:
                print("Error. Please type in a number with no punctuation or variables.Please round to the nearest dollar. ")
        while True:
            additionalexpenses = input("Do you have any other forms of monthly expenses (Ex: LawnSnowCare/Vacancy/Repairs/CapitalExpenditures/PropertyManagement)? If so, list the total estimate here: ")
            if additionalexpenses.isnumeric():
                self.finance['AddExpenses'] = additionalexpenses
                break
            else:
                print("Error. Please type in a number with no punctuation or variables.Please round to the nearest dollar. ")
        self.finance['TotalExpenses'] = int(mortgage) + int(expenses) + int(additionalexpenses)
        print(f"Your total expenses is {self.finance['TotalExpenses']}")
        
    def squarethree(self):
        while True:
            if 'TotalIncome' in self.finance and 'TotalExpenses' in self.finance:
                self.finance['CashFlow'] = int(self.finance['TotalIncome']) - int(self.finance['TotalExpenses'])
                print(f"Your Cash Flow is estimated: {self.finance['CashFlow']}")
                return
            else:
                print("Please fill out your expenses and income information before calculating Cash Flow!")
                break

    def squarefour(self):
        while True:
            dpayment = input("How much was the down payment on your house? ")
            if dpayment.isnumeric():
                self.finance['DownPayment'] = dpayment
                break
            else:
                print("Error. Please type in a number with no punctuation or variables.Please round to the nearest dollar. ")
        while True: 
            closingcosts = input("How much was the closing costs on your house? ")
            if closingcosts.isnumeric():
                self.finance['ClosingCost'] = closingcosts
                break
            else:
                print("Error. Please type in a number with no punctuation or variables.Please round to the nearest dollar. ")
        while True: 
            renovations = input("How much were the repairs/renovations, if any? Please add any other miscellaneous investments as well. ")
            if renovations.isnumeric():
                self.finance['Renovations/Repairs'] = renovations
                break
            else:
                print("Error. Please type in a number with no punctuation or variables.Please round to the nearest dollar. ")
        self.finance['TotalInvestment'] = int(dpayment) + int(closingcosts) + int(renovations)
        print(f"Your total investment is {self.finance['TotalInvestment']}")

    def roi(self):
         while True:
            if 'CashFlow' in self.finance and 'TotalInvestment' in self.finance:
                roi = ((self.finance['CashFlow'])/(self.finance['TotalInvestment'])) * 100
                print(f"Your Return on Investment is {roi}%")
                return
            else:
                print("Please fill out ALL your information before calculating ROI!")
                break

    def data(self):
        print(self.finance)


homeowner = Roi(2000)
def run():
    while True:
        entrance = input("Welcome to Brandon's ROI Calculator! Please to select a section: Income,Expenses,CashFlow,Investments,ROI,ShowMyData ").lower()
        if entrance == 'income':
            homeowner.squareone()
        elif entrance == 'expenses':
            homeowner.squaretwo()
        elif entrance == 'cashflow':
            homeowner.squarethree()
        elif entrance == 'investments':
            homeowner.squarefour()
        elif entrance == 'roi':
            homeowner.roi()
        elif entrance == 'showmydata':
            homeowner.data()
        else:
            print("Invalid Entry. Please try again.")

run()
