def loop(res, matrix, top, left, bottom, right):
    x = left
    y = top
    while (x <= right and y <= bottom):
        res.append(matrix[y][x])
        x = x + 1
    x = x - 1
    top = top + 1
    y = y + 1
    while (y <= bottom and x <= right):
        res.append(matrix[y][x])
        y = y + 1
    y = y - 1
    right = right - 1
    x = x - 1
    if (top <= bottom):
        while (x >= left and y>= top):
            res.append(matrix[y][x])
            x = x - 1
        x = x + 1
        bottom = bottom - 1
        y = y - 1
    if (left <= right):
        while (y >= top and x >= left):
            res.append(matrix[y][x])
            y = y -1
    return res


def spiralOrder(matrix):
    nrows = len(matrix)
    ncols = len(matrix[0])
    top = 0
    left = 0
    bottom = nrows -1
    right = ncols - 1
    res = []
    while (top <= bottom and left <= right):
        res = loop(res, matrix, top, left, bottom, right)
        top = top + 1
        left = left + 1
        bottom = bottom - 1
        right = right - 1
    return res

mat = [[1,2,3],[4,5,6],[7,8,9]]

print(spiralOrder(mat))

mat2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
        
print(spiralOrder(mat2))

mat3 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
        
print(spiralOrder(mat3))

mat4 = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
        
print(spiralOrder(mat4))

mat5 = [[3],[2]]
        
print(spiralOrder(mat5))

mat7 = [[2,5],[8,4],[0,-1]]

print(spiralOrder(mat7))

mat6 = [[7],[9],[6]]

print(spiralOrder(mat6))

