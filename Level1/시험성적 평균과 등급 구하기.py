if __name__ == "__main__":

    score = list(map(int, input().split()))

    average = sum(score) / 3
    grade = 'default'

    if average >= 90:
        grade = 'A'
    elif average >= 80:
        grade = 'B'
    elif average >= 70:
        grade = 'C'
    elif average >= 60:
        grade = 'D'
    else:
        grade = 'F'

    # print("{0} {1}".format(round(average, 2), grade))
    print("%.2f %c" % (average, grade))  # 자동 반올림