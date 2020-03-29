if __name__ == "__main__":

    coordinate = []
    max_x, max_y = 0, 0

    for i in range(3):
        coordinate.extend(map(int, input().split()))

    # 삼각형 조건 확인(기울기 활용)
    slope_1 = (coordinate[3] - coordinate[1]) / (coordinate[2] - coordinate[0])
    slope_2 = (coordinate[5] - coordinate[3]) / (coordinate[4] - coordinate[2])

    if slope_1 == slope_2:
        print("0.00")
    else:
        coordinate[2] -= coordinate[0]
        coordinate[3] -= coordinate[1]
        coordinate[4] -= coordinate[0]
        coordinate[5] -= coordinate[1]

        result = abs(((coordinate[2] * coordinate[5]) - coordinate[3] * coordinate[4]) * 1/2)

        print("%.2f" %result)


