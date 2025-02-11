# Problem: X-Sum - https://codeforces.com/problemset/problem/1676/D

from collections import defaultdict
def solve():
    rows, cols = [int(i) for i in input().split()]
    mat = [[int(i) for i in input().split()] for _ in range(rows) ]

    main = defaultdict(int)
    second = defaultdict(int)
    curr_sum = 0
    maxim_val = 0

    for row in range(rows):
        for col in range(cols):
            main[row - col] += mat[row][col]
            second[row + col] += mat[row][col]
    
    for row in range(rows):
        for col in range(cols):
            curr_sum = main[row - col] + second[row + col] - mat[row][col]
            maxim_val = max(maxim_val, curr_sum)     

    print(maxim_val)

t = int(input())
for _ in range(t):
    solve()