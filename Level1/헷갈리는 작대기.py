if __name__ == "__main__":

    cnt = {"1": 0, "I": 0, "l": 0, "|": 0}

    string = input()
    
    for i in string:
        if i in cnt.keys():
            cnt[i] += 1
        
    print(cnt["1"])
    print(cnt["I"])
    print(cnt["l"])
    print(cnt["|"])

