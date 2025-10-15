class Employee:
    company = "Perplexity"

    def __init__(self, name, salary, age):
        self.name = name
        self.salary = salary
        self.age = age

    def profile(self):
        return f"{self.name} earns {self.salary}Rs "

    @classmethod
    def change_company(cls, name):
        cls.name = name

    def which_generation(self):
        return "Older" if self.age > 18 else "Younger"

    @staticmethod
    def is_salary_valid(salary):
        return "Salary is Valid" if salary > 0 else "Invalid"


emp1 = Employee("Harman", 80000, 24)
emp2 = Employee("Amar", 90000, 48)
emp3 = Employee("Vanshika", 100000, 27)
emp4 = Employee("Jason", 135000, 54)
print(emp1.profile())
print(emp1.which_generation())
print(emp4.profile())
print(emp1.which_generation())
print(emp2.profile())
print(emp2.is_salary_valid())
