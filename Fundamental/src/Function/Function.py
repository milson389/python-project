# Python Function


def square(x):
    return x * x


a = 10
s = square(a)
print('{} Square is {}'.format(a, s))


def changeMe(myList):
    myList.append([1, 2, 3, 4])
    print('Value inside the function: {}'.format(myList))


yourList = [10, 20, 30]
changeMe(yourList)
print('Value outside the function: {}'.format(yourList))


def printInfo(name, age=20):
    print('Name: ', name)
    print('Age: ', age)


printInfo(age=5, name="Dicoding")
printInfo(name="Audie")


def printInformation(fixedarg, *args):
    print('Output: fixedarg {}'.format(fixedarg))
    for a in args:
        print('Position Argument {}'.format(a))


printInformation(10)
printInformation(70, 60, 50)


def infoPrint(*args, **kwargs):
    for a in args:
        print('Position Agrument {}'.format(a))
    for key, value in kwargs.items():
        print('Keyword Argument {}: {}'.format(key, value))


infoPrint()
infoPrint(1, 2, 3)
infoPrint(i=7, j=8, k=9)
infoPrint(1, 2, j=8, k=9)
infoPrint(*(2, 3), **{'i': 7, 'j': 8})

# Anonymous Function
# lambda [arg1 [,arg2,........argn]]:expression

sum__ = lambda arg1, arg2: arg1 + arg2
print("Value of total: ", sum__(10, 20))