if __name__ == "__main__":

    n = int(input())
    data = list(map(int, input().split()))
    result = []

    for i in range(len(data)):
        if data[i] & -data[i] != data[i]:
            result.append(i + 1)

    print(len(result))
    print(" ".join(map(str, result)))