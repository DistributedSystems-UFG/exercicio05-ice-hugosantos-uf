import sys, Ice
import Demo
 
communicator = Ice.initialize(sys.argv)

try:
    printerBase = communicator.stringToProxy("SimplePrinter:default -p 11000")
    calculatorBase = communicator.stringToProxy("SimpleCalculator:default -p 11000")

    printer = Demo.PrinterPrx.checkedCast(printerBase)
    calculator = Demo.CalculatorPrx.checkedCast(calculatorBase)

    if not printer:
        raise RuntimeError("Invalid printer proxy")

    if not calculator:
        raise RuntimeError("Invalid calculator proxy")

    printer.printString("Hello World!")
    printer.printUpper("texto enviado para a funcao printUpper")
    printer.printLower("TEXTO ENVIADO PARA A FUNCAO printLower")

    calculator.addNumbers(10, 5)
    calculator.multiplyNumbers(10, 5)
finally:
    communicator.destroy()
