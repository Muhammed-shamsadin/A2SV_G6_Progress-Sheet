# Problem: Books - https://codeforces.com/contest/279/problem/B

n, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]

l, r = 0, 0
curr_sum = 0
max_len = 0

while r < n:
    curr_sum += a[r]

    while curr_sum > k:
        curr_sum -= a[l]
        l += 1
    
    max_len = max(max_len, r - l + 1)
    
    r += 1

print(max_len)