import csv
class School:
    Schools = []

    def __init__(self, school_name, bank_account, yearly_income=0):
        self.school_name = school_name
        self.bank_account = bank_account
        self.yearly_income = yearly_income
        School.Schools.append(self)

    def __repr__(self):
        return f'(School: {self.school_name})'

    def calculate_net_income(self):
        yearly_income = self.yearly_income
        tax = SchoolFinance.calculate_school_tax(yearly_income)
        self.yearly_income -= tax
        return f'{self.school_name} yearly income is {self.yearly_income}'    
    
class SchoolFinance:
    HIGH_TAX = 0.2
    LOW_TAX = 0.12
    RETIRMENT_COST = 0.05
    INSURANCE = 100

    @staticmethod
    def calculate_school_tax(yearly_income):
        if yearly_income > 300000:
            tax = yearly_income * SchoolFinance.HIGH_TAX    
        else:
            tax = yearly_income * SchoolFinance.LOW_TAX
        return tax
    
    @staticmethod
    def calculate_teacher_deductions(gross_salary):
        if gross_salary > 2500:
            tax = gross_salary *  SchoolFinance.HIGH_TAX
            total_deductions = tax + SchoolFinance.INSURANCE + (gross_salary * SchoolFinance.RETIRMENT_COST)
        
        else:
            tax = gross_salary *  SchoolFinance.LOW_TAX
            total_deductions = tax + SchoolFinance.INSURANCE + (gross_salary * SchoolFinance.RETIRMENT_COST)              
        
        return total_deductions    

    @staticmethod
    def calculate_net_salary(gross_salary):
        net_salary = gross_salary - SchoolFinance.calculate_teacher_deductions(gross_salary)    
        return net_salary    

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

    @classmethod
    def create_instances(cls, file_name):
        with open(file_name) as f:
            teachers = csv.DictReader(f)
            for teacher in teachers:
                name = teacher.get('name')    
                school_name = teacher.get('school_name')    
                id = teacher.get('id')    
                bank_account = teacher.get('name')    
                phone = teacher.get('phone')
                hours_worked = teacher.get('hours_worked')
                hourly_rate = teacher.get('hourly_rate')
                Teacher(name, school_name, id, bank_account, phone, hours_worked, hourly_rate)    

class Teacher:
    Teachers = {}
    AllTeachers = []
    def __init__(self, name, school, id, bank_account, phone, hours_worked=150, hourly_rate=12):
        self.name = name
        self.school = school
        self.__id = id
        self.__bank_account = bank_account
        self.phone = phone
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
        Teacher.AllTeachers.append(self)

    def __repr__(self):
        return f'(Teacher: {self.name} works at {self.school} )'    

    @property
    def bank_account(self):
        return self.__bank_account

    @property 
    def id(self):
        return self.__id

    def login(self):
        user_name = input('please enter your username: ')
        if user_name != Teacher.Teachers[self.name]['user_name']:
            print('Invalid username')
        else:
            password = input('please enter your password: ')    

    def calculate_gross_salary(self):
        return self.hourly_rate * self.hours_worked

    def calculate_net_salary(self):
        gross_salary = self.calculate_gross_salary()
        net_salry = SchoolFinance.calculate_net_salary(gross_salary)    
        return f'{self.name} net salary is {net_salry}'

class Manager(Teacher):
    pass

ali = Teacher('ali', 'osi', '1234', '12222', '23')
