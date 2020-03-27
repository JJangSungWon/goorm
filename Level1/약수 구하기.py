import math

if __name__ == "__main__":

    n = int(input())
    result = []

    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            result.append(i)
            result.append(int(n / i))

    # set을 이용하여 중복 제거
    result = sorted(list(set(result)))

    # print(" ".join(map(str, result)))
    # 제일 마지막에 공백을 추가해야해서 for문으로 대체
    for data in result:
        print(data, end=" ")
