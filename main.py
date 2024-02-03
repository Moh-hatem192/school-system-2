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
    
    @classmethod
    def list_schools(cls):
        for i, school in enumerate(School.Schools, 1):
            print(f'{i}: {school.school_name}')

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
    def create_school_instances(cls, file_name):
        with open(file_name) as f:
            schools = csv.DictReader(f)
            for school in schools:
                school_name = school.get('School_name')    
                bank_account = school.get('Bank_account')    
                yearly_income = school.get('yearly_income')
                School(school_name, bank_account, yearly_income)    

    @classmethod
    def create_teachers_instances(cls, file_name):
        with open(file_name) as f:
            teachers = csv.DictReader(f)
            for teacher in teachers:
                name = teacher.get('name')    
                school_name = teacher.get('school_name')    
                id = teacher.get('id')    
                bank_account = teacher.get('bank_account')    
                phone = teacher.get('phone')
                hours_worked = teacher.get('hours_worked')
                hourly_rate = teacher.get('hourly_rate')
                Teacher(name, school_name, id, bank_account, phone, hours_worked, hourly_rate)    

class Teacher:
    Teachers = {
        'Islam Hesham':{
            'user_name': 'islam23',
            'password': '1234',
            'school': 'Codezilla'
        },
        'Mohammed Gouda':{
            'user_name': 'moh123',
            'password': '1234',
            'school': 'Codezilla'
        },
        'Ahmad Ibrahim':{
            'user_name': 'ahmad123',
            'password': '1234',
            'school': 'Omareyah'
        },
        'Ismaeel Yousef':{
            'user_name': 'Ismaeel1234',
            'password': '1234',
            'school': 'Omareyah'
        },
        'Yousef khlewee':{
            'user_name': 'yousef1234',
            'password': '1234',
            'school': 'Oxford'
        },
        'Hatem Ahmad':{
            'user_name': 'hatem123',
            'password': '1234',
            'school': 'Oxford'
        },
        'Khalid Saeed':{
            'user_name': 'khalid1234',
            'password': '1234',
            'school': 'Itihad'
        }
    }
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

    @classmethod
    def login(cls):
        user_name = input('please enter your username: ')
        if user_name not in Teacher.Teachers.keys():
            print('Invalid username')
            
        elif Teacher.Teachers[user_name]['school'] != school_name:
            print("Sorry you don't work at this school")    
        
        else:
            while True:
                password = input('please enter your password: ') 
                if password == Teacher.Teachers[user_name]['password']:
                    print('Login successefull')
                    break
                else:
                    print('incorrect password try again')       

    def calculate_gross_salary(self):
        return self.hourly_rate * self.hours_worked

    def calculate_net_salary(self):
        gross_salary = self.calculate_gross_salary()
        net_salry = SchoolFinance.calculate_net_salary(gross_salary)    
        return f'{self.name} net salary is {net_salry}'

class Manager(Teacher):
    BONUS = 550
    

def main():
    print('Welcome to the Schools online system: ')
    SchoolInstances.create_school_instances('Schools.csv')
    SchoolInstances.create_teachers_instances('Teachers.csv')
    while True:
        School.list_schools()
        choice = input('Please chose your school: ')
        try:
            int(choice)
        except:
            print('Please enter a valid choice')  
            continue
        if int(choice) <1 or int(choice) > 4:
            print('Please enter a valid choice')
            continue        
        choice = int(choice)
        global school_name
        school_name = School.Schools[choice - 1].school_name
        print(f'Welcome to {school_name} school')
        Teacher.login()

main()    
