class word():
    def __init__(self): #constructor for a class. The self parameter refers to the instance of the object.
        self.s = ""

    def getString(self):
        self.s = input("Please insert word: ")

    def printString(self):
        print(self.s.upper())

strObj = word()
strObj.getString()
strObj.printString()
