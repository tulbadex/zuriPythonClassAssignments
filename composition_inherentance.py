class Employee:

    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

    def check_salary(self):
        return self.salary.check_salary()


class Salary:

    def __init__(self, amount, bonus):
        self.amount = amount
        self.bonus = bonus/100

    def check_salary(self):
        return f"Marketer's salary is {self.amount + (self.amount * self.bonus)} with a bonus of {self.bonus}"

marketer_salary = Salary(400000, 5)
marketer = Employee('Mike', 'marketting', marketer_salary)
print(marketer.check_salary())