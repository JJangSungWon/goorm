if __name__ == "__main__":
    num, change_num = input().split()

    if num == change_num:
        if len(num) > 1:
            print(10)
        else:
            print(int(num) + 1)
    else:
        for i in range(2, 17):
            result = 0
            val = 1

            for j in range(1, len(change_num) + 1):
                if change_num[-j] >= 'A':
                    if i > ord(change_num[-j]) - 55:
                        value = ord(change_num[-j]) - 55
                    else:
                        break
                else:
                    value = int(change_num[-j])

                result += value * val
                val *= i

            if result == int(num):
                print(i)
                break
