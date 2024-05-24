def fib(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    return fib(x - 1) + fib(x - 2)


print(f'{fib(10)}')
# use recursive funtion when it is tree shaped and requrie parent-child connection.


def factoral(x):
    if x == 1:
        return 1
    return factoral(x - 1) * x


print(f'{factoral(6)}')


def fibWithoutRecursive(x):
    if x == 0:
        return [0]
    elif x == 1:
        return [0, 1]

    sequence = [0, 1]

    for i in range(2, x + 1):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


n = 10
print(f'{fibWithoutRecursive(n)}')

# if tree does not work, use array 


