if __name__ == "__main__":

    total = 0

    limit = int(input())

    for i in range(1, limit + 1):
        if i % 3 == 0 or i % 5 == 0:
            total += i

    print(total)