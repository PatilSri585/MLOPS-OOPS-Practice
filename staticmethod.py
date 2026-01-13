class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def is_adult(age):
        return age >= 18
    
    def is_human(self):
        print(f'{self.name} is a human being.')
    
harsha = person("Harsha", 20)
print(harsha.name)  # Output: Harsha
print(harsha.age)   # Output: 20


harsha.is_human()  # Output: Harsha is a human being.
person.is_human(harsha)  # Output: Harsha is a human being.
print(harsha.is_adult(20))  # Output: True # Static method called using instance and do not use self keyword
print(person.is_adult(17))  # Output: False # Static method called using class name and do not use self keyword