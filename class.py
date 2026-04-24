class EMP:
    raise_amount = 1.04
    num_of_emps = 0
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        EMP.num_of_emps += 1
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        self.method = 'apply_raise'

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
        #pass

class Dev(EMP):
    raise_amount = 1.10
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang
class Manager(EMP):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

print(EMP.num_of_emps)
emp1=EMP('John', 'Doe', 50000)
print(EMP.num_of_emps)
emp2=EMP('Jane', 'Smith', 60000)
dev1=Dev('Bob', 'Johnson', 70000, 'Python')
manager1=Manager('Alice', 'Williams', 80000, [emp1, emp2, dev1])
manager1.print_emps()
manager1.add_emp(EMP('Charlie', 'Brown', 55000))
manager1.print_emps()
manager1.remove_emp(emp1)
manager1.print_emps()

