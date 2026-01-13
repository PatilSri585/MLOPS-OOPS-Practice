class animal:
    def __init__(self,name):
        self.name = name

    def sound(self):
        print(f'{self.name} makes sound')

class dog(animal):
    def sound(self):
        print(f'{self.name} will bark')

buddy = animal("Buddy")

buddy.sound()

tommy = dog("tommy")
tommy.sound()