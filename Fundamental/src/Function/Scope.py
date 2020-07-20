# Python variable scope

total = 0  # global variable


def sums(arg1, arg2):
    global total
    total = arg1 + arg2
    print('Inside the function: {}'.format(total))
    return total


sums(10, 20)
print('Outside the function (global) total: {}'.format(total))