a = 5
print(a, "is of type", type(a))
a = 2.0
print(a, "is of type", type(a))
a = 1+2j
print(a, "is complex number?", isinstance(1+2j, complex))

animal = ['cat', 'rabbit', 'tiger', 'wolf']
del animal[1]
print(animal)

print(int('2+3'))