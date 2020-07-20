# Python List
# Collection with Ordered Sequence

a = [1, 2.2, 'Python']
x = [5, 10, 15, 20, 25, 30, 35, 40]
print(x[5])
print(x[-1])
print(x[3:5])
print(x[:5])
print(x[-3:])
print(x[1:7:2])
print(x[1:7:3])

x = [1, 2, 3]
# to change list element
x[2] = 4
print(x)

# to add new element into the list
x.append(5)
print(x)

# to remove element from the list
spam = ['cat', 'bat', 'rat', 'elephant']
del spam[2]
print(spam)