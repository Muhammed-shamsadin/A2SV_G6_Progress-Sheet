# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]

    maxim = a[0]
    summ = 0
    right = 1

    while right < n:
        if a[right - 1] * a[right] > 0:
            maxim = max(maxim, a[right])
        else:   
            summ += maxim 
            maxim = a[right]
        right += 1

    summ += maxim  
    
    print(summ)

