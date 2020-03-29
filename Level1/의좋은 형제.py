if __name__ == "__main__":

    n1, n2 = map(int, input().split())
    d = int(input())

    for i in range(1, d + 1):
        if i % 2 == 0:
            if n2 % 2 == 0:
                n1 += n2 // 2
                n2 -= n2 // 2
            else:
                n1 += n2 // 2 + 1
                n2 -= n2 // 2 + 1
        else:
            if n1 % 2 == 0:
                n2 += n1 // 2
                n1 -= n1 // 2
            else:
                n2 += n1 // 2 + 1
                n1 -= n1 // 2 + 1

    print(n1, n2)