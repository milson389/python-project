# Python Input Output

# Output

# Combine directly variable with String
a = 5
print('The value of A is ', a)

# Using String Format Mechanism
print('Hello {}'.format('brother'))

# Using % operator and argument specifiers
name = "John"
age = 15
print("Hello, %s!" % name)
print("%s is %d years old." % (name, age))

myList = [1, 2, 3]
print("A list: %s" % myList)

# Argument Specifiers :
# 1. %s - String
# 2. %d - Integers
# 3. %f - Float
# 4. %.<digit>f - Double
# 5. %x/%X - Hexa representation of Integers

a, b = 10, 11
print('a: %x and b: %X' % (a, b))

# Input

num = input('Enter a number: ')
print(num)

# eval() Function to solve Mathematics Expression
print(eval('2+3'))

