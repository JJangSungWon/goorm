if __name__ == "__main__":

    vowel = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    K = int(input())

    for i in range(K):
        string = input()
        result = []

        for j in range(len(string)):
            if string[j] in vowel:
                result.append(string[j])
        if len(result) == 0:
            print("???")
        else:
            print("".join(result))

