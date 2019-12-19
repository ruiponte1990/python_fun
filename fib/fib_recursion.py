def main(n):
    if n < 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return  main(n-1) + main(n-2)


if __name__ == "__main__":
    print(main(5))
    print(main(3))
    print(main(10))
    # stack blows up, this solution is impractical
    # print(main(100))