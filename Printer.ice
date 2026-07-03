module Demo
{
    interface Printer
    {
        void printString(string s);
        void printUpper(string s);
        void printLower(string s);
    }

    interface Calculator
    {
        void addNumbers(int a, int b);
        void multiplyNumbers(int a, int b);
    }
}
