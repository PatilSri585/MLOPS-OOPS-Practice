class example:
    def __init__(self):
        pass
    def withselfonly(self):
        print("This is printed with self only")
    def withothers(self,name):
        print("This is printed with self and others including")

obj = example()    
withself = obj.withselfonly()
# withothersalso = obj.withothers() -- This expects an argument. so throws error.
withothersalso = obj.withothers("Harsha")