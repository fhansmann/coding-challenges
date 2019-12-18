class word():
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input("Please insert word: ")

    def printString(self):
        print(self.s.upper())

strObj = word()
strObj.getString()
strObj.printString()
