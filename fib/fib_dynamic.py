fibArr = [0,1]

def main(n):
    if n < 0:
        return 0
    elif n <= len(fibArr):
        return fibArr[n-1]
    else:
        tmp = main(n-1) + main(n-2)
        fibArr.append(tmp)
        return tmp



if __name__ == "__main__":
    print(main(5))
    print(main(3))
    print(main(10))
    print(main(100))