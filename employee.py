"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salary, contract,commission, commission_type, commission_total, contract_total, hours_worked):
        self.name = name
        self.salary = salary
        self.contract = contract
        self.commission = commission
        self.commission_type = commission_type
        self.commission_total = commission_total
        self.contract_total = contract_total
        self.hours_worked = hours_worked

    def get_pay(self):
        payment = 0
        if self.contract == "monthly":
            payment = get_monthly(self)
        else:
            payment = get_hourly(self)

        return payment

    def get_monthly(self):
        payment = 0
        if self.commission == False:
            payment = self.salary
        elif self.commission and self.commission_type == "bonus":
            payment = self.salary + self.commission_total
        else:
            payment = self.salary + (self.contract_total * self.commission_total)

        return payment

    def get_hourly(self):
        payment = 0
        if self.commission == False:
            payment = self.salary * self.hours_worked
        elif self.commission and self.commission_type == "bonus":
            payment = (self.salary * self.hours_worked) + self.commission_total
        else:
            payment = (self.salary * self.hours_worked) + (self.contract_total * self.commission_total)

        return payment

    def __str__(self):
        final_string = ""

        if self.contract == "monthly":
            final_string = monthly_string(self)
        else:
            final_string = hourly_string(self)

        return final_string

    def monthly_string(self):
        final_string = ""
        if self.commission == False:
            final_string += f'{self.name} works on a monthly salary of {self.salary}. Their total pay is {self.get_pay()}.'
        elif self.commission and self.commission_type == "bonus":
            final_string += f'{self.name} works on a monthly salary of {self.salary} and receives a bonus commission of {self.commission_total}. Their total pay is {self.get_pay()}.'
        else:
            final_string += f'{self.name} works on a monthly salary of {self.salary} and receives a commission for {self.contract_total} contract(s) at {self.commission_total}/contract. Their total pay is {self.get_pay()}.'

        return final_string

    def hourly_string(self):
        final_string = ""
        if self.commission == False:
            final_string += f'{self.name} works on a contract of {self.salary} hours at {self.hours_worked}/hour. Their total pay is {self.get_pay()}.'
        elif self.commission and self.commission_type == "bonus":
            final_string += f'{self.name} works on a contract of {self.salary} hours at {self.hours_worked}/hour and receives a bonus commission of {self.commission_total}. Their total pay is {self.get_pay()}.'
        else:
            final_string += f'{self.name} works on a contract of {self.salary} hours at {self.hours_worked}/hour and receives a commission for {self.contract_total} contract(s) at {self.commission_total}/contract. Their total pay is {self.get_pay()}.'

        return final_string


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')
