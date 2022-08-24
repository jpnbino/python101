
class Employee:

    raise_amt = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        
        self.pay = pay
    
    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first , last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Deletou o maluco!')
        self.first = None
        self.last = None

    def apply_raise (self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod 
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

#inheritance 
class Developer(Employee):
    raise_amt = 2

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname)

#print(help(Developer))

Employee.set_raise_amt(1.5)
print(Employee.raise_amt)
 
dev1 = Developer('joao', 'daqui', 50000, 'Python')
dev2 = Employee('Dudu', 'de lá', 50000)
mng1 = Manager('Edu','Doidao', 30000, [dev1])
mng1.add_emp(dev2)
mng1.print_emps()

print(dev1.email)
print(dev1.pay)
print(dev2.pay)
dev1.apply_raise()
dev2.apply_raise()
print(dev1.pay)
print(dev2.pay)


dev1.fullname = 'Cachorro doido'
print (dev1.first)
print (dev1.last)

del dev1.fullname