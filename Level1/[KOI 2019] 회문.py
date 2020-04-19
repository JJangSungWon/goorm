import sys
import copy

if __name__ == "__main__":
    T = int(sys.stdin.readline())

    for _ in range(T):

        string = list(input().strip())

        if string == string[::-1]:
            print(0)
        else:
            lyes, ryes = True, True
            l, r = 0, len(string) - 1
            check = False

            # 왼쪽부터 확인
            while l <= r:
                if string[l] != string[r]:
                    if not check:
                        check = True
                        r -= 1
                    else:
                        lyes = False  # 2번 이상 다르다
                        break
                else:
                    l += 1
                    r -= 1

            l, r = 0, len(string) - 1
            check = False

            # 오른쪽부터 확인
            while l <= r:
                if string[l] != string[r]:
                    if not check:
                        check = True
                        l += 1
                    else:
                        ryes = False
                        break
                else:
                    l += 1
                    r -= 1

            if not (lyes | ryes):
                print(2)
            else:
                print(1)
