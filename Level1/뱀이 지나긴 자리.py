if __name__ == "__main__":

    N, M = map(int, input().split())
    flag = 1
    for i in range(N):
        if i % 2 == 0:
            print("#" * M)
        else:
            if flag == 1:
                print("." * (M -1) + "#")
            else:
                print("#" + ("." * (M - 1)))

            flag *= -1