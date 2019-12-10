import sys
import numpy as np

def rotate(mat):
    # will need to change this algorithm so it can be called on smaller and smaller matrices
    # call it on outermost. then call it on next level in, then next level in
    l = len(mat)
    for i in range(1, l):
        tmp = mat[i][0]
        mat[i][0] = mat[i-1][0]
    mat[l-1][0] = tmp
    for i in range(1, l):
        tmp = mat[l-1][i]
        mat[l-1][i] = mat[l-1][i-1]
        

def main(path):
    mat = np.loadtxt(path, dtype='i', delimiter=',')
    return rotate(mat)

if __name__ == "__main__":
    print(main(sys.argv[1]))