if __name__ == "__main__":

    original = ['b', 'i', 'l', 'm', 'n', 'o', 'p', 's', 'u', 'v', 'w', 'x']
    copy = ['d', 'i', 'l', 'm', 'n', 'o', 'q', 'z', 'u', 'v', 'w', 'x']

    T = int(input())

    for i in range(T):
        data = list(input())
        reversed_data = list(reversed(data))
        flag = 1

        for j in range(len(data)):
            if data[j] in original:
                if reversed_data[j] not in copy:
                    flag = 0
                else:
                    if original.index(data[j]) != copy.index(reversed_data[j]):
                        flag = 0
            elif data[j] in copy:
                if reversed_data[j] not in original:
                    flag = 0
                else:
                    if copy.index(data[j]) != original.index(reversed_data[j]):
                        flag = 0
            else:
                flag = 0

        if flag:
            print("Mirror")
        else:
            print("Normal")
