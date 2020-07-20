# Python String and List Manipulation

# len() Function
l = [1, 2, 3, 3, 4, 4, 4, 4, 5, 6]
s = set(l)
x = "Hello, World"

print(l)
print(len(l))

print(s)
print(len(s))

print(x)
print(len(x))

# Combination and Replication
# Combination with (+)

print([1, 2, 3] + ['A', 'B', 'C'])
spam = [1, 2, 3]
spam += ['A', 'B', 'C']
print(spam)

# Replication with (*)

print(['x', 'y', 'z'] * 3)
arr = [0]*10
print(len(arr))
print(arr)
print('=====')

# range()
# give a series of numbers with certain patterns
# for loops, to access list element
# range() can have 1-3 parameters

for i in range(9):
    print(i)

print('=====')

for i in range(3, 9):
    print(i)

print('=====')

# range(1, 9, 2) = range( from, until, difference/distance )
print([_ for _ in range(1, 9, 2)])  # list comprehension

for i in range(1, 9, 2):
    print(i)

print('=====')

# in and not in
# to know if a value/object are inside the list we can use the in and not in operator
# this function return booleans value

sample = ['hello', 'hi', 'howdy', 'heyas']
print('howdy' in sample)
print('howdy' not in sample)
print('cat' in sample)
print('cat' not in sample)
print('=====')

# Assign value to more than 1 variable at once

# from list
cat = ['fat', 'orange', 'loud']
size, color, disposition = cat
print(size, color, disposition)

# from tuple
cat = ('fat', 'orange', 'loud')
size, color, disposition = cat
print(size, color, disposition)

# Multi variables assignment can be used to switch 2 or more variable's value
a, b = 'Alice', 'Bob'
a, b = b, a
print(a)
print(b)

# Python sort() method
# can't sort list that contains String and Numbers at once
# sort method using the ASCII order so capital letter are printed first the lower case letter

x = [2, 5, 3.14, 1, -7]
x.sort()
print(x)

y = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
y.sort()
print(y)

y.sort(reverse=True)
print(y)

m = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
m.sort()
print(m)

# to handle sort orders problem we can use the str.lower method
spam = ['a', 'z', 'A', 'z']
spam.sort(key=str.lower)
print(spam)
