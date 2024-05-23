def triangle(z):
    for x in range(z):
        A = 2 * x + 1
        S = z - x - 1
        T = S * ' ' + A * 'A'
        print(T)
triangle(4)

def flip_triangle(z):
    for x in range(z):
        A = 2 * (z - x - 1) + 1
        S = x
        T = S * ' ' + A * 'A'
        print(T)
flip_triangle(4)

def right_triangle(z):
    for x in range(z):
        A = x + 1
        S = z - x
        T = S * ' ' + A * 'A'
        print(T)
    for y in range(z - 1):
        a = z - y - 1
        s = z - a + 1
        t = s * ' ' + a * 'A'
        print(t)
right_triangle(4)

def left_triangle(z):
    for x in range(z):
        A = x + 1
        S = 3 - x
        T = A * 'A' + S * ' '
        print(T)
    for y in range(z - 1):
        a = z - y - 1
        s = - 1 * y + 1
        t = a * 'A' + s * ' '
        print(t)
left_triangle(4)

def diamond(z):
    for x in range(z - 1):
        A = 2 * x + 1
        S = z - x - 1
        T = S * ' ' + A * 'A'
        print(T)
    for x in range(z):
        A = 2 * (z - x - 1) + 1
        S = x
        T = S * ' ' + A * 'A'
        print(T)
diamond(4)
