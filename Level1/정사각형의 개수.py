import math

if __name__ == "__main__":

    n = int(input())

    if n == 1:
        print(1)
    else:
        result = 0
        while n >= 1:

            copy_n = n
            while copy_n >= 1:
                result += copy_n * copy_n
                copy_n = math.ceil(copy_n / copy_n - 1)

            n -= 1

        print(result)