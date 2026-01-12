class employee:
    def __init__(self):
        print('started executing attribues/data')
        self.id = 101
        self.salary = 20000
        self.designation = "Software Engineer"
        print('finished executing attribues/data')


    def travel(self,destination):
        print('started executing Method')
        print(f'Employee is now travelling to {destination}')
        print('Finished executing Method')

Harsha = employee()
# Harsha.travel("Ooty")                                      
# print(Harsha.salary)
print(type(Harsha))