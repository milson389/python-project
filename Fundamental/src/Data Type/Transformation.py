# Python Data Type Transformation

x = 1
print(type(x))
print(str(x).zfill(5))

# Character and Strings Transformation

# UpperCase
p = 'Hello World!'
p = p.upper()
print(p)

# LowerCase
p = p.lower()
print(p)

feeling = input('How are you ?')
if feeling.lower() == 'great':
    print('I feel great too.')
else:
    print('I hope the rest of your day is good')

# isX Method from String for Checking
print('Method isX from String for Checking')
# 1. isalpha() = return true if String only contains word and not empty
# 2. isalnum() = return true if String only contains word or number and not empty
# 3. isdecimal() = return true if String only contains number/numeric and not empty
# 4. isspace() = return true if String only contains space, tab, newline, or whitespaces, and not empty
# 5. istitle() = return true if String's first char are capital letter and continued by lower case letter
# 6. islower() = return true if String only contains lower case letter
# 7. isupper() = return true if String only contains upper case letter

p = 'Hello World'
print(p, '.islower() = ', p.islower())
print(p, '.isupper() = ', p.isupper())

p = 'HELLO WORLD'
print(p, '.isupper() = ', p.isupper())

print('hello.isalpha() = ', 'hello'.isalpha())
print('hello123.isalpha() = ', 'hello123'.isalpha())
print('hello123.isalnum() = ', 'hello123'.isalnum())
print('hello.isalnum() = ', 'hello'.isalnum())
print('123.isdecimal() = ', '123'.isdecimal())
print('   .isspace() = ', '   '.isspace())
print('This Is Title Case.istitle() = ', 'This Is Title Case'.istitle())
print('This Is not Title Case.istitle() = ', 'This Is not Title Case'.istitle())
print('This Is NOT Title Case Either.istitle() = ', 'This Is NOT Title Case Either'.istitle())

# startswith() and endswith() method from String
print('Hello World.startswith(\'Hello\') = ', 'Hello World'.startswith('Hello'))
print('Hello World.endswith(\'World \') = ', 'Hello World'.endswith('World'))

# join() and split() method from String
# join() -> the string that operated with this function will be added between each parameter/argument

print(', '.join(['cats', 'rats', 'bats']))
print(' '.join(['My', 'name', 'is', 'Milson']))
print('ABC'.join(['My', 'name', 'is', 'Simon']))

# split() -> split substring by specific delimiter ( default delimiter : whitespace, space, tab, newline)

print('My name is Simon'.split())
print('MyABCnameABCisABCSimon'.split('ABC'))
print('My name is Simon'.split('m'))

# Text alignment rjust(), ljust(), center()
print('Hello'.rjust(10, '*'))
print('Hello'.ljust(10, '*'))
print('Hello'.center(10, '='))

# Removing White space with strip(), lstrip(), rstrip()
spam = '     Hello World     '
print(spam)
print(spam.strip())
print(spam.lstrip())
print(spam.rstrip())
spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('ampS'))

# replace() function to change String/Substring
text = "Ayo belajar Coding di Dicoding"
print(text.replace("Coding", "Pemrograman"))
text = "Ayo belajar Coding di Dicoding karena Coding adalah bahasa masa depan"
print(text.replace("Coding", "Pemrograman", 1))