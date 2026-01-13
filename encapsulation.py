class employee:
    def __init__(self):
        self.name = "Employee1"     #normal
        self.id = 123               #normal
        self.designation = 'SDE'    #normal
        self.__salary = 40000       #encapsulated


harsha = employee()
print(harsha.name)
print(harsha.designation)
print(harsha.id)
print(harsha.__salary)              #cant be accessed.AttributeError: 'employee' object has no attribute '__salary'
print(harsha._employee__salary)      #Can be accessed like this. Output: 40000