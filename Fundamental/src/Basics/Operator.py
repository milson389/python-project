# Python Operator and Operand
# 1. + = add
# 2. - = subtract
# 3. * = multiplication
# 4. ** = power/ exponentiation
# 5. / = divide ( float )
# 6. // = divide ( int ) floor division
# 7. % = modulo
# 8. @ = matrix multiplication

# Bit Operation
# 1. << = left shift, 2<<2 = 8 -> ( 2 = 10 in binary, so 10 2x << = 1000 = 8 )
# 2. >> = right shift, 11>>1 = 5 -> ( 11 = 1011 in binary, so 1x >> = 101 = 5 )
# 3. & = bit wise And, 5&3 = 1 -> ( 5 = 101 , 3 = 011 -> 1&0 = 0, 0&1 = 0, 1&1 = 1, so 001 = 1 )
# 4. | = bit wise or, 5|3 = 7 -> ( 5 = 101, 3 = 011 -> 1|0 = 1, 0|1 = 1, 1|1 = 1, so 111 = 7 )
# 5. ^ = bit wise XOR, 5^3 = 6 -> ( 5 = 101, 3 = 011 -> 101 xor 011 = 1xor0 = 1, 0xor1 = 1, 1xor1 = 0, so 110 = 6 )
# 6. ~ = bit wise invert, ~5 = -6 -> ( ~5 = -(5+1) = -(6) = -6 )

# Comparison
# 1. < ( less than ) [lt]
# 2. > ( greater than ) [gt]
# 3. <= ( less than or equal to ) [le]
# 4. >= ( greater than or equal to ) [ge]
# 5. == ( equal to ) [eq]
# 6. != ( not equal to ) [ne]

# Boolean
# 1. not
# 2. and
# 3. or

from operator import *
a = 1
b = 5.0
print('a = {}'.format(a))
print('b = {}'.format(b))
for func in (lt, le, eq, ne, ge, gt):
    print('{}(a, b): {}'.format(func.__name__, func(a, b)))


