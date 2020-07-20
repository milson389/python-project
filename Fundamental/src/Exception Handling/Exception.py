# Python Exception Handling

import sys

z = 0
try:
    x = 1/z
    print(x)
except ZeroDivisionError:
    print('Cannot divided by zero')

try:
    with open('test.py') as file:
        print(file.read())
except (FileNotFoundError):
    print('File not found')


d = {'average': '10.0'}
try:
    print('Average: {}'.format(d['average']))
except KeyError:
    print('Key not found in dictionary')
except ValueError:
    print('Value not match the key')

try:
    print('Average: {}'.format(d['average']/3))
except KeyError:
    print('Key not found in dictionary')
except (ValueError, TypeError):
    print('Value or type mismatch')

try:
    print('Rounded Average: {}'.format(int(d['average'])))
except (ValueError, TypeError) as e:
    print('Exception Handling: {}'.format(e))