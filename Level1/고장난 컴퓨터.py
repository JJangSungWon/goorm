if __name__ == "__main__":
    
    n, c = map(int, input().split())
    arr = list(map(int, input().split()))
    
    pre, cnt = arr[0], 1
    for i in range(1, len(arr)):
        if arr[i] - pre > c:
            cnt = 1
            pre = arr[i]
        else:
            cnt += 1
            pre = arr[i]
    
    print(cnt)
        
        