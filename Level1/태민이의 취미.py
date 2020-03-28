import math

if __name__ == "__main__":
    
    n = int(input())
    
    total = n * (n+1) // 2 % 1000000007
    answer = total * total % 1000000007
    print(answer)