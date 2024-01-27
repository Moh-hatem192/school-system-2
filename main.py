import csv
class School:
    Schools = []

    def __init__(self, school_name, bank_account, yearly_income):
        self.school_name = school_name
        self.bank_account = bank_account
        self.yearly_income = yearly_income
        School.Schools.append(self)

    def __repr__(self):
        return f'(School: {self.school_name})'

    def calculate_net_income(self):
        yearly_income = self.yearly_income
        tax = SchoolFinance.calculate_tax(yearly_income)
        self.yearly_income -= tax
        return f'{self.school_name} yearly income is {self.yearly_income}'    
    
class SchoolFinance:
    HIGH_TAX = 0.25
    LOW_TAX = 0.15

    @staticmethod
    def calculate_tax(yearly_income):
        if yearly_income > 300000:
            tax = yearly_income * SchoolFinance.HIGH_TAX    
        else:
            tax = yearly_income * SchoolFinance.LOW_TAX
        return tax

class SchoolInstances:
    @classmethod
    def create_instances(cls, file_name):
        with open(file_name) as f:
            schools = csv.DictReader(f)
            for school in schools:
                school_name = school.get('School_name')    
                bank_account = school.get('Bank_account')    
                yearly_income = school.get('yearly_income')
                School(school_name, bank_account, yearly_income)    

class Teacher:
    pass

class Manager(Teacher):
    pass