if __name__ == "__main__":

    T = int(input())
    data = []

    for i in range(T):
        data.append(int(input()))

    cnt = 0
    value = -1
    for i in range(len(data)-1, -1, -1):
        if value < data[i]:
            value = data[i]
            cnt += 1

    print(cnt)
