class InputOut:
    def __init__(self, name, age, address):
        self.name=""
        self.age=0
        self.address=""
    def getString(self):
        self.name=input("What's your name'? ")
        self.age=input("And age? ")
        self.address=input("What about address? ")
    def printString(self):
        print(self.name.capitalize())
        print(self.age)
        print(self.address.upper())
strObj=InputOut("Bink", 19, "Hai Duong")
strObj.getString()
strObj.printString()