

# for x in range(7):
#     hiddenSpace = 0
#     if x >= 1:
#         hiddenSpace = 1
#     else:
#         hiddenSpace = 0

#     A = 1
#     if A == 1 and A == 6:
#         A = ' '
#     else:
#         A = 'A'

#     zero1 = x - 1
#     zero2 = 5 - x
#     y = hiddenSpace * ' ' + '0' * zero1 + A + (zero2) * '0'
    
#     print(y)


# zeros = ''
# for x in range(6):
#     zeros = '0' * x
#     zero = ' ' + zeros

# print(zero)

# for x in range(1, 6):
#     hiddenSpace = 0
#     if x >= 1:
#         hiddenSpace = 1
#     else:
#         hiddenSpace = 0

#     A = 1
#     if A == 1 and A == 6:
#         A = ' '
#     else:
#         A = 'A'

#     zero1 = x - 1
#     zero2 = 5 - x
#     y = hiddenSpace * ' ' + '0' * zero1 + A + (zero2) * '0'
#     print(y)


# print(zero)


zeros = ''
for x in range(6):
    zeros = '0' * x
    zero = ' ' + zeros

print(zero)

for x in range(0, 6):
    hiddenSpace = 0
    if x >= 0:
        hiddenSpace = 1
    else:
        hiddenSpace = 0

    A = 1
    if A >= 1 and A <= 6:
        A = 'AA'
    else:
        A = ' '
    
    b = ''

    zero1 = x - 1
    zero2 = (4 - x)
    y = hiddenSpace * ' ' + '0' * zero1 + b + A + (zero2) * '0'

    if hiddenSpace <= 1 and x == 0:
        A = ''
        b = 'A'
        y = hiddenSpace * ' ' + '0' * zero1 + b + A + (zero2) * '0'
    else:
        y = hiddenSpace * ' ' + '0' * zero1 + b + A + (zero2) * '0'

    if zero2 >= -1 and x == 5:
        A = ''
        b = 'A'
        y = hiddenSpace * ' ' + '0' * zero1 + b + A + (zero2) * '0'
    else:
        y = hiddenSpace * ' ' + '0' * zero1 + b + A + (zero2) * '0'

    print(y)

print(zero)