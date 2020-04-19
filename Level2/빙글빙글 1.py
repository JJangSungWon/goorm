if __name__ == "__main__":

    N = int(input())
    copy_N = N
    data = [[' '] * N for _ in range(N)]

    i, j = 0, 0
    val = 1
    # 첫 줄 완성
    for j in range(N):
        data[0][j] = '#'
    N -= 1

    while N >= 0:
        for _ in range(N):
            i += val
            data[i][j] = '#'

        val *= -1
        for _ in range(N):
            j += val
            data[i][j] = '#'
        N -= 2

    for i in range(len(data)):
        print(" ".join(map(str, data[i])))
