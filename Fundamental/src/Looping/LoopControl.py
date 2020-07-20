# Python Loop Control

for letter in 'Python':
    if letter == 'h':
        break
    print('Current letter : {}'.format(letter))

var = 10
while var > 0:
    print('Current variable value: {}'.format(var))
    var -= 1
    if var == 5:
        break

# Continue
for letter in 'Python':
    if letter == 'h':
        continue
    print('Current letter : {}'.format(letter))

for a in [0, 1, -1, 2, -2, 3, -3]:
    if a <= 0:
        continue
    print('Element positif: {}'.format(a))

var = 10
while var > 0:
    var -= 1
    if var == 5:
        continue
    print('Current variable value: {}'.format(var))

# Else after for
for n in range(2, 10):
    for x in range(2, n):
        if n%x == 0:
            print(n, 'equals', x, '*', n/x)
            break
        else:
            print(n, ' is not a factor of ', x)

# Else after while
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
else:
    print('Loop is finished')

# Pass, used when you want a block of statement, but that statement won't do anything and continue the execution
for letter in 'Python':
    if letter == 'h':
        pass
        print('This is pass block')
    print('Current letter: {}'.format(letter))

for letter in 'Python':
    if letter.isupper():
        pass
    else:
        print('Lower letter: {}'.format(letter))

# Exception handling
import sys

data = ''
while data != 'exit':
    try:
        data = input('Please enter an integer ( type exit to exit ): ')
        print('got integer: {}'.format(int(data)))
    except:
        if data == 'exit':
            pass
        else:
            print('Error : {}'.format(sys.exc_info()[0]))

# List Comprehension, make a list with inline loop and if

# Traditional Way
numbers = [1, 2, 3, 4]
squares = []
for n in numbers:
    squares.append(n**2)
print(squares)

# List Comprehension way
# new_list = [expression for_loop_one_or_more condition]

numbers = [1, 2, 3, 4]
squares = [n**2 for n in numbers]
print(squares)

# Find similar element between 2 list

#Traditional
list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]
common_num = []
for a in list_a:
    for b in list_b:
        if a == b:
            common_num.append(a)

print(common_num)

# List Comprehension
list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]
common_num = [a for a in list_a for b in list_b if a == b]
print(common_num)

list_a = ["Hello", "World", "In", "Python"]
small_list_a = [_.lower() for _ in list_a]
print(small_list_a)

list_a = range(1, 10, 2)
x = [[a**2, a**3] for a in list_a]
print(x)
