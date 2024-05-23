def triangle(rows):
    for a in range(rows):
        As = 2 * a + 1
        space = rows - a - 1
        row = ' ' * space + 'A' * As
        print(row)


triangle(4)


def flippedTriangle(rows):
    for a in range(rows):
        As = 2 * (rows - a - 1) + 1
        space = a
        row = ' ' * space + 'A' * As
        print(row)


flippedTriangle(4)


def Right_side_triangle(rows):
    totalRows = 2 * rows - 1
    for a in range(totalRows):
        if a < rows:
            As = a + 1
        else:
            As = (totalRows - a - 1) + 1
        row = 'A' * As
        print(row)


Right_side_triangle(4)


def Left_side_triangle(rows):
    for a in range(rows * 2 - 1):
        space = abs(rows - a - 1)
        As = rows - space
        row = ' ' * space + 'A' * As
        print(row)


Left_side_triangle(4)
