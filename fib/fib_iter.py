def main(n):
    first = 0
    second = 1
    if n < 0:
        return first
    elif n == 0:
        return first
    elif n == 1:
        return second
    else:
        for i in range(2, n):
            next_ = second + first
            first = second
            second = next_
        return second
   

if __name__ == "__main__":
    print(main(5))
    print(main(3))
    print(main(10))
    print(main(100))