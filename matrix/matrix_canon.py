import sys
import numpy as np
import math

def main(path):
    mat = np.loadtxt(path, dtype='i', delimiter=',')
    rev = np.flip(mat, 1)
    trans = np.transpose(rev)
    return trans
    

if __name__ == "__main__":
    print(main(sys.argv[1]))