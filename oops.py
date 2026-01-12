class employee:
    def __init__(self):
        self.id = 101
        self.salary = 20000
        self.designation = "Software Engineer"


    def travel(self,destination):
        print(f'Employee is now travelling to {destination}')

Harsha = employee()
Harsha.travel("Ooty")
# print(Harsha.salary)