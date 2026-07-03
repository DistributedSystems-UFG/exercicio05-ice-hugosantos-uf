import sys, Ice
import Demo
 
class PrinterI(Demo.Printer):
    def printString(self, s, current=None):
        print(s)

    def printUpper(self, s, current=None):
        print(s.upper())

    def printLower(self, s, current=None):
        print(s.lower())

class CalculatorI(Demo.Calculator):
    def addNumbers(self, a, b, current=None):
        print(f"{a} + {b} = {a + b}")

    def multiplyNumbers(self, a, b, current=None):
        print(f"{a} x {b} = {a * b}")

communicator = Ice.initialize(sys.argv)

try:
    adapter = communicator.createObjectAdapterWithEndpoints("SimpleAdapter", "default -p 11000")
    printer = PrinterI()
    calculator = CalculatorI()

    adapter.add(printer, communicator.stringToIdentity("SimplePrinter"))
    adapter.add(calculator, communicator.stringToIdentity("SimpleCalculator"))
    adapter.activate()

    print("Servidor iniciado.")
    communicator.waitForShutdown()
finally:
    communicator.destroy()
