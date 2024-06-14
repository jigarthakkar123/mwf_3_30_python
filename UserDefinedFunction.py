'''
Function is a set of instruction that perform a specific task.
1. Function With No Argument & No Return Value.
2. Function With Argument But No Return Value.
3. Function With Argument & Return Value.
'''
def printLine():
    print("*"*50)

printLine()
print("This is user defined function in python.")
printLine()

def add(a,b):
    print("Addition : ",a+b)

printLine()
add(10,20)
printLine()

def sub(a,b):
    return a-b

printLine()
#ans=sub(10,20)
print("Subtraction : ",sub(10,20))
printLine()
