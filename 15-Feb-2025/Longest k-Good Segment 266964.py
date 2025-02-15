# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

from collections import defaultdict

n, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]

window = defaultdict(int)
l, r = 0, 0 
max_len = 0
ans = []

for r in range(n):
    window[a[r]] += 1

    while len(window) > k:
        window[a[l]] -= 1
        if window[a[l]] == 0:
            del window[a[l]]
        l += 1

    if max_len < r - l + 1:
        max_len = r - l + 1
        ans = [l + 1, r + 1]


print(*ans)
