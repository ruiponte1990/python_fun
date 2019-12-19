def main(n):
    first = 0
    second = 1
    i = 2
    while True:
        if (i > n):
            return
        else:
            yield second 
            next_ = second + first
            first = second
            second = next_
            i += 1

if __name__ == "__main__":
    print(list(main(5))[-1])
    print(list(main(3))[-1])
    print(list(main(10))[-1])