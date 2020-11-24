import sys 
import copy

def findTarget(acc, a, i, j, target, path):
    if i < len(a):
        if j < len(a[i]):
            val = a[i][j] * acc
            if val > target:
                return False
            elif val == target and i == (len(a) - 1):
                return path
            else:
                L = path + "L"
                R = path + "R"
                left = findTarget(val, a, i+1, j, target, L)
                if left: return left
                right = findTarget(val, a, i+1, j+1, target, R)
                if right: return right
        else:
            return False
    else:
        return False




if __name__ == '__main__':
    file1 = open(sys.argv[1], 'r')
    lines = file1.readlines()
    file1.close()
    a = []
    target = int(lines.pop(0).strip("\n").split(":")[1])
    for line in lines:
        s = line.strip("\n").split(",")
        s = list(map(int, s))
        a.append(s)
    x = findTarget(1, a, 0, 0, target, "")
    file2 = open(sys.argv[2],'w')
    file2.write(x)
    file2.write("\n")
    file2.close()