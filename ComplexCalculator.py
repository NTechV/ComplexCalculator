from cmath import cos, log, sin, tan
from math import ceil, floor
from ComplexA import Add
from ComplexA import Subtract
from ComplexA import Multiplication
from ComplexA import Divison
from some_tools import modify_File

def power(base,exponet):
    result = 1
    for index in range(exponet):
        result = result * base
    return result
def cube(number):
    return number * number * number
print("Enter operator (+) addition (-) subtraction (*) multiplication (\) divison")
print("s for sine, r for rounding, l for log,cl for ceil, f for floor, c for cos")
print("t for tangent,p for power, sq for square, and cc for cube")
op = input(": ")

if op == "+":
    fnum1 = float(input("Enter first number: "))
    fnum2 = float(input("Enter second number: "))
    t = (fnum1,fnum2)
    x = Add(t[0],t[1])
    print("Result: " + str(x.add()))
    modify_File("ar.txt",str(x.add()) + "\n")
if op == "-":
    fnum1 = float(input("Enter first number: "))
    fnum2 = float(input("Enter second number: "))
    t = (fnum1,fnum2)
    x = Subtract(t[0],t[1])
    print("Result: " + str(x.sub()))
    modify_File("ar.txt", str(x.sub()) + "\n")
if op == "*":
    fnum1 = float(input("Enter first number: "))
    fnum2 = float(input("Enter second number: "))
    t = (fnum1,fnum2)
    x = Multiplication(t[0],t[1])
    print("Result: " + str(x.mul()))
    modify_File("ar.txt",str(x.mul()) + "\n")
if op == "/":
    try:
        fnum1 = float(input("Enter first number: "))
        fnum2 = float(input("Enter second number: "))
        t = (fnum1,fnum2)
        x = Divison(t[0],t[1])
        print("Result: " + str(x.div()))
        modify_File("ar.txt",str(x.div()) + "\n")
    except:
        print("Exception has occured!")
if op == "s":
    fnum = float(input("Enter a number: "))
    result = sin(fnum)
    print("Result: " + str(result))
    modify_File("ar.txt",str(result) + "\n")
if op == "l":
    fnum = float(input("Enter a number: "))
    result = log(fnum)
    print("Result: " + str(result))
    modify_File("ar.txt",str(result) + "\n")
if op == "c":
    fnum = float(input("Enter a number: "))
    result = cos(fnum)
    print("Result: " + str(result))
    modify_File("ar.txt",str(result) + "\n")
if op == "sq":
    fnum = float(input("Enter a number: "))
    result = fnum * fnum
    print("Result: " + str(result))
    modify_File("ar.txt",str(result) + "\n")
if op == "t":
    fnum = float(input("Enter a number: "))
    result = tan(fnum)
    print("Result: " + str(result))
    modify_File("ar.txt",str(result) + "\n")
if op == "p":
    fnum = int(input("Enter a base: "))
    fnum1 = int(input("Enter the power: "))
    result = power(fnum,fnum1)
    print("Result: " + str(result))
    modify_File("ar.txt",str(result) + "\n")

if op == "f":
    fnum = float(input("Enter a number: "))
    result = floor(fnum)
    print("Result: " + str(result))
    modify_File("ar.txt",str(result) + "\n")
if op == "cc":
    fnum = float(input("Enter a number: "))
    result = cube(fnum)
    print("Result: " + str(result))
    modify_File("ar.txt",str(result) + "\n")
if op == "cl":
    fnum = float(input("Enter a number: "))
    result = ceil(fnum)
    print("Result: " + str(result))
    modify_File("ar.txt",str(result) + "\n")







