import sys
import numpy as np
import math

def fullRotate(mat):
    for _ in range(len(mat)-1):
        mat = rotate(mat)
    return mat

def rotate(mat):
    l = len(mat)
    tmp1 = mat[0][0]
    for i in range(1, l):
        tmp2 = mat[i][0]
        mat[i][0] = tmp1
        tmp1 = tmp2
    for i in range(1, l):
        tmp2 = mat[l-1][i]
        mat[l-1][i] = tmp1
        tmp1 = tmp2
    for i in range(l-2, -1, -1):
        tmp2 = mat[i][l-1]
        mat[i][l-1] = tmp1
        tmp1 = tmp2
    for i in range(l-2, -1, -1):
        tmp2 = mat[0][i]
        mat[0][i] = tmp1
        tmp1 = tmp2
    return mat

def main(path):
    mat = np.loadtxt(path, dtype='i', delimiter=',')
    l = len(mat)
    med = int(math.floor(len(mat)/2))
    for i in range(0, med+1):
        sub_mat = mat[i:(l-i)]
        sub = []
        for j in sub_mat:
            sub.append(j[i:(l-i)])
        sub_mat = fullRotate(sub)
    return mat

if __name__ == "__main__":
    print(main(sys.argv[1]))