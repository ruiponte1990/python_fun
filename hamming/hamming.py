
def hammingDistance(self, x, y):
    xBits = self.makeBitArray(x)
    yBits = self.makeBitArray(y)
    diff = 0
    for i in range(0, 32):
        if xBits[i] != yBits[i]:
            diff = diff + 1
    return diff
    
def makeBitArray(self, num):
    zeros = [0]*32
    sum = 0
    for i in range(0, 32):
        if (sum + 2**(31-i)) <= num:
            zeros[i] = 1
            sum = sum + 2**(31-i)
    return zeros