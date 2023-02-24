def spiralOrder(mat):
    res = []
    while mat:
        res += mat.pop(0)
        if mat and mat[0]:
            for line in mat:
                res.append(line.pop())
        if mat:
            res += mat.pop()[::-1]
        if mat and mat[0]:
            for line in mat[::-1]:
                res.append(line.pop(0))
    return res

mat = [[1,2,3],[4,5,6],[7,8,9]]

print(spiralOrder(mat))

mat2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
        
print(spiralOrder(mat2))

mat3 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
        
print(spiralOrder(mat3))

mat4 = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
        
print(spiralOrder(mat4))

testMat = [[3],[2]]
        
print(spiralOrder(testMat))