# Problem: Insertion Sort - https://www.hackerrank.com/challenges/insertionsort1/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    val = arr[-1]  # The last element to be placed correctly
    j = n - 2  # Start comparing from the second last element
    
    # Shift elements to the right until we find the correct spot for `val`
    while j >= 0 and arr[j] > val:
        arr[j + 1] = arr[j]  # Shift element
        print(*arr)  # Print after each shift
        j -= 1  
    
    arr[j + 1] = val  # Place `val` in its correct position
    print(*arr)
        
    return arr
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
