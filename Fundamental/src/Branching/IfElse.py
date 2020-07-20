# Python If Conditional

var1 = 100
if var1:
    print("1 - Got a true expression value")
    print(var1)
var2 = 0
if var2:
    print("2 - Got a true expression value")
    print(var2)

# If Else Statement
amount = int(input("Enter amount: "))
if amount<1000:
    discount = amount*0.05
    print("Discount", discount)
else:
    discount = amount*0.10
    print("Discount", discount)

print("Net payable: ", amount-discount)

a = 8
if a%2 == 0:
    print('bilangan {} adalah genap'.format(a))
else:
    print('bilangan {} adalah ganjil'.format(a))

# Elif Statement
amount = int(input("Enter amount: "))
if amount<1000:
    discount = amount*0.05
    print("Discount", discount)
elif amount<5000:
    discount = amount * 0.10
    print("Discount", discount)
else:
    discount = amount*0.15
    print("Discount", discount)

print("Net payable: ", amount-discount)